from django.conf.urls import url
from PU import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^tasks/$', views.TasksList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TasksDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)