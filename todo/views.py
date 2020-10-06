from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from .models import Task

def index(request):
  latest_task_list = Task.objects.order_by('-target').reverse()
  context = {'latest_task_list': latest_task_list}
  return render(request, 'todo/index.html', context)

def new(request):
  latest_task_list = Task.objects.all()
  if request.method == 'POST':
    form = TaskForm(data=request.POST)
    # print(form.errors)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('index'))

  return render(request, 'todo/index.html', {'latest_task_list': latest_task_list, 'form': form})


def delete(request, task_id):
  task = get_object_or_404(Task, pk=task_id)
  task.delete()
  return HttpResponseRedirect(reverse('index'))

def edit(request, task_id):
  if request.method == 'POST':
    task = Task.objects.get(pk=task_id)
    print(task)
    print(request.POST)
    task.task=request.POST['task']
    task.target=request.POST['target']
    task.save()
    return HttpResponseRedirect(reverse('index'))
  else:
    latest_task_list = Task.objects.all()
    context = {'latest_task_list': latest_task_list}
    return render(request, 'todo/index.html', context)