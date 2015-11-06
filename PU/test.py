from django.contrib.auth.models import User
from django.test.client import Client
import requests
import unittest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from PU.models import Tasks
from PU.serializers import TasksSerializer

__author__ = 'pisar_iv'

#====================================Tasks==============================================================================

class TasksTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TasksTestCase, cls).setUpClass()
        cls.client = APIClient()
        cls.user = User.objects.create_user('Ivan', 'ex@mple.re', 123123)
        cls.task = Tasks(pk=2,task_des = 'des',task_date = None,owner = cls.user,task_ok = False)
        cls.task.save()


    @classmethod
    def tearDownClass(cls):
        super(TasksTestCase, cls).tearDownClass()
        cls.user.delete()
        cls.task.delete()


    def setUp(self):
        super(TasksTestCase, self).setUp()
        user = User.objects.get(username = 'Ivan')
        self.client.force_authenticate(user=user)


    def test_create_task(self):
        response = self.client.post(reverse('TaskList'),{"task_des":"des"},format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_task_list(self):
        response = self.client.get(reverse('TaskList'),  format = 'json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_task_detail(self):
        response_detail = self.client.get(reverse('TaskDetail',args=[self.task.id]),  format = 'json')
        self.assertEqual(response_detail.status_code,status.HTTP_200_OK)


    def test_update_task(self):
        data = TasksSerializer(self.task).data
        response = self.client.put(reverse('TaskDetail', args=[self.task.id]),{'task_des':'123123123jgg' , 'task_ok':True},format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_task_list_report(self):
        response = self.client.get(reverse('PrintReport'),  format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    """def test_delete_task(self):
        data = TasksSerializer(self.task).data
        response = self.client.delete(reverse('TaskDetail',args=[self.task.id]),data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)"""


#=============================Users=====================================================================================

class UserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(UserTest, cls).setUpClass()
        cls.client = APIClient()
        cls.user = User.objects.create_superuser('Ivan','ex@mple.re',123123)
        cls.test_user = User.objects.create_user('Foo','ex@mple.re',123123)
        cls.test_user.save()

    @classmethod
    def tearDownClass(cls):
        super(UserTest, cls).tearDownClass()
        cls.user.delete()
        cls.test_user.delete()

#Admin

    def setUp(self):
        super(UserTest, self).setUp()
        user = User.objects.get(username='Ivan')
        self.client.force_authenticate(user=user)

    def test_user_admin_create(self):
        response = self.client.post(reverse('UserList'), {'username':'Kurt','password':'123'}, format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_user_admin_get(self):
        response = self.client.get(reverse('UserList'), format = 'json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_user_admin_update(self):
        response = self.client.patch(reverse('UserDetail',args = [self.test_user.id]), {'username':'FooFoo'}, format = 'json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    """def test_user_admin_delete(self):
        response = self.client.delete(reverse('UserDetail',args=[self.test_user.id]), format = 'json')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)"""

#Users

    def test_userAccount_update(self):
        response = self.client.patch(reverse('UserAccount',args = [self.user.id]), {'email':'Ivan@ml.ru'}, format = 'json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_userSwitchPassword(self):
        response = self.client.patch(reverse('UserPassword',args = [self.user.id]), {'password':'123123','new_password':'123'})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
































