# coding=utf-8
from __future__ import unicode_literals
import os
from django.http import HttpResponse

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from secretary import Renderer
from PU.models import Tasks
from PU.serializers import TasksSerializer,UserSerializer,UserPasswordSerializer,UserPatchSerializer
from rest_framework import filters
from rest_framework import generics
import django_filters
from django.contrib.auth.models import User

#=======================================================================================================================
#Tasks
from untitled import settings


class TasksList(generics.ListCreateAPIView):
    serializer_class = TasksSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Tasks.objects.all()
        else:
            return Tasks.objects.filter(owner = self.request.user)

    queryset = Tasks.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('task_des', 'task_date')


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TasksSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Tasks.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Tasks.objects.all()
        else:
            return Tasks.objects.filter(owner = self.request.user)

#=======================================================================================================================
#Admin

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

#=======================================================================================================================
#Users

class UserAccount (generics.UpdateAPIView):

    serializer_class = UserPatchSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        if self.request.user.id == int(kwargs['pk']):
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("Обращение не к своему аккаунту")

    def patch(self, request, *args, **kwargs):
        if self.request.user.id == int(kwargs['pk']):
            return self.partial_update(request, *args, **kwargs)
        else:
            raise ValidationError("Обращение не к своему аккаунту")


class UserPassword (generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPasswordSerializer
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        if self.request.user.id == int(kwargs['pk']):
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("Обращение не к своему аккаунту")

    def patch(self, request, *args, **kwargs):
        if self.request.user.id == int(kwargs['pk']):
            return self.partial_update(request, *args, **kwargs)
        else:
            raise ValidationError("Обращение не к своему аккаунту")




#=======================================================================================================================
#Report

class PrintReport(APIView):

    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        engine = Renderer()
        template = os.path.join(settings.BASE_DIR, 'static', 'template.odt')
        context = {
        'taskList' : Tasks.objects.filter(owner=self.request.user),
        'DOC_NAME' : 'Reropt',
        }
        result = engine.render(template, **context)
        response = HttpResponse(content_type = 'application/odt',content = result)
        response['Content-Disposition'] = 'attachment; filename="renders.odt"'
        return response




