from django.db import models
from django.utils import timezone

class Task(models.Model):
  task = models.CharField(max_length=100, null=False)
  completed = models.BooleanField(default=False)
  target = models.DateTimeField()

  def __str__(self):
    return self.task

  def expired(self):
    return self.target >= timezone.now()

