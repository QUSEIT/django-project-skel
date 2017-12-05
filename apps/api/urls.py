#coding:utf-8
from django.conf.urls import url
from .views import views, user_views


#base
urlpatterns = [
    url('^example', views.Example.as_view()),
    url('^user/list', user_views.UserList.as_view())
]