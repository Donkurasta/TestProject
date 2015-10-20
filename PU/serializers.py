from django.contrib.gis import serializers
from rest_framework import serializers
from PU.models import Tasks
from django.contrib.auth.models import User

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id','task_des','task_date','task_ok')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username','email','password')
