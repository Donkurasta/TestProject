from django.db import models

class Tasks(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks')
    task_des = models.CharField(max_length=200)
    task_date = models.DateTimeField('date limit', blank=True, null=True)
    task_ok = models.BooleanField(default=False)

