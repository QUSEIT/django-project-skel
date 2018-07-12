#coding:utf-8
"""（后台管理）
一个urlpatterns 对应一个views文件,
一个views对应一个models(apps.models.xx_models)
"""
from django.conf.urls import url #patterns
from apps.backs.views import views


urlpatterns = [
    url(r'^$', views.ManagerLogin.as_view()),
    url(r'^login$', views.ManagerLogin.as_view()),
    url(r'^login_out$', views.ManagerLoginOut.as_view()),
    url(r'^index$', views.ManagerIndex.as_view()),
]

urlpatterns +=[
    
]
