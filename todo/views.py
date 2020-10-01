from django.shortcuts import render

from .models import Task

def index(request):
  latest_task_list = Task.objects.all()
  context = {'latest_task_list': latest_task_list}
  return render(request, 'todo/index.html', context)
