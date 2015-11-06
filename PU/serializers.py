import re
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.gis import serializers
from rest_framework import serializers
from PU.models import Tasks
from django.contrib.auth.models import User
from secretary import Renderer

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id','task_des','task_date','task_ok')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username','email','password')


class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name',)


class UserPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        new_password = validated_data.get('new_password')
        salt = instance.password.split('$')[2]
        hashed_password = make_password(password, salt)
        if (password != new_password) and (instance.password == hashed_password):
            instance.set_password(new_password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance
