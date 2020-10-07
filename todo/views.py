from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from .models import Task
from django.utils import timezone
import datetime


def render_index(request):
  now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
  task_list = Task.objects.filter(completed='False').order_by('-target').reverse()
  completed_task = Task.objects.filter(completed='True').order_by('-target')
  context = {'task_list': task_list, 'completed_task': completed_task, 'now': now}
  return render(request, 'todo/index.html', context)


def index(request):
  return render_index(request)

def new(request):
  if request.method == 'POST':
    form = TaskForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('index'))
  else:
    form = TaskForm()
  return render_index(request)


def delete(request, task_id):
  task = get_object_or_404(Task, pk=task_id)
  task.delete()
  return HttpResponseRedirect(reverse('index'))

def edit(request, task_id):
  task = get_object_or_404(Task, pk=task_id)
  if request.method == 'POST':
    task.task=request.POST['task']
    task.target=request.POST['target']
    task.save()
    return HttpResponseRedirect(reverse('index'))
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
      return HttpResponseRedirect(reverse('index'))
    else:
      task.completed = request.POST['completed']
      task.save()
      return HttpResponseRedirect(reverse('index'))
  else:
    return render_index(request)