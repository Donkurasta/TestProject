from rest_framework import serializers
from PU.models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id','task_des','task_date','task_ok')


