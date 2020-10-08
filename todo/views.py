from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from .models import Task
from accounts.forms import LoginForm
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required

@login_required

def render_index(request, form=None):
  user = request.user
  now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
  utc_time = timezone.now()
  task_list = Task.objects.filter(completed='False', author_id=user.id).order_by('-target').reverse()
  completed_task = Task.objects.filter(completed='True', author_id=user.id).order_by('-target')
  context = {'task_list': task_list, 'completed_task': completed_task, 'now': now, 'utc_time': utc_time, 'form': form}
  return render(request, 'todo/index.html', context)


def index(request):
  return render_index(request)

def new(request):
  if request.method == 'POST':
    user = request.user
    form = TaskForm(data=request.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.author_id = user.id
      task.save()
      return HttpResponseRedirect(reverse('todo:index'))
    else:
      form.add_error(None, 'タスクが未入力です')
      return render_index(request, form)


def delete(request, task_id):
  task = get_object_or_404(Task, pk=task_id)
  task.delete()
  return HttpResponseRedirect(reverse('todo:index'))

def edit(request, task_id):
  task = get_object_or_404(Task, pk=task_id)
  if request.method == 'POST':
    form = TaskForm(data=request.POST)
    if form.is_valid():
      task.task=request.POST['task']
      task.target=request.POST['target']
      task.save()
      return HttpResponseRedirect(reverse('todo:index'))
    else:
      return render_index(request)
  else:
    return render_index(request)

def completed(request, task_id):
  now = timezone.now()
  task = get_object_or_404(Task, pk=task_id)
  if request.method == 'POST':
    if request.POST['completed'] == 'True':
      task.completed =request.POST['completed']
      task.target = now
      task.save()
      return HttpResponseRedirect(reverse('todo:index'))
    else:
      task.completed = request.POST['completed']
      task.save()
      return HttpResponseRedirect(reverse('todo:index'))
  else:
    return render_index(request)