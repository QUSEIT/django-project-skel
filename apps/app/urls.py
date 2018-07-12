#coding:utf-8
from django.conf.urls import url, include
from apps.app.views import views

urlpatterns = [
    url(r'^$', views.Index.as_view())
]
