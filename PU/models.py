from django.db import models

class Tasks(models.Model):
    task_des = models.CharField(max_length=200)
    task_date = models.DateTimeField('date limit', blank=True, null=True)
    task_ok = models.BooleanField(default=False)
