from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    task = forms.CharField(min_length=1, max_length=100, required=True)
    completed = forms.BooleanField(required=False)
    target = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        required=True,
      )


    class Meta:
        model = Task
        fields = ('task', 'completed', 'target')