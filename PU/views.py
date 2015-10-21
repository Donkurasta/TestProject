# coding=utf-8
from __future__ import unicode_literals


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from PU.models import Tasks
from PU.serializers import TasksSerializer,UserSerializer
from rest_framework import filters
from rest_framework import generics
import django_filters
from django.contrib.auth.models import User

class TasksList(generics.ListCreateAPIView):
    serializer_class = TasksSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Tasks.objects.all()
        else:
            return Tasks.objects.filter(owner=self.request.user)
    queryset = Tasks.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('task_des', 'task_date')


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()

class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def delete(self, request, *args, **kwargs):
        if self.request.user.id == int(kwargs['pk']):
            raise ValidationError("Нельзя удалить себя!")
        else:
            return self.destroy(request, *args, **kwargs)


