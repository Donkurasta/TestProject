from PU.models import Tasks
from PU.serializers import TasksSerializer
from rest_framework import filters
from rest_framework import generics
import django_filters

class TasksList(generics.ListCreateAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('task_des', 'task_date')


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()


