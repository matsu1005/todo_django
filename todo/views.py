from django.shortcuts import render
# from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
from .forms import TaskForm
from .models import Task

def index(request):
  latest_task_list = Task.objects.all()
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
  else:
    form = TaskForm()

  return render(request, 'todo/index.html',
                           {'latest_task_list': latest_task_list, 'form': form})

  