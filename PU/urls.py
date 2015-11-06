from django.conf.urls import url
from PU import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^tasks/$', views.TasksList.as_view(),name = 'TaskList'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TasksDetail.as_view(),name = 'TaskDetail'),

    url(r'^userinf/$', views.UserList.as_view(), name = 'UserList'),
    url(r'^userinf/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'UserDetail'),

    url(r'^account/(?P<pk>[0-9]+)/$', views.UserAccount.as_view(), name = 'UserAccount'),
    url(r'^password/(?P<pk>[0-9]+)/$', views.UserPassword.as_view(), name = 'UserPassword'),

    url(r'^tasksreport/$', views.PrintReport.as_view(), name = 'PrintReport'),
]
urlpatterns = format_suffix_patterns(urlpatterns)