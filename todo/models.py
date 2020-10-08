from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
  task = models.CharField(max_length=100, null=False)
  completed = models.BooleanField(default=False)
  target = models.DateTimeField()
  author = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
  )

  def __str__(self):
    return self.task

  def expired(self):
    return self.target >= timezone.now()

