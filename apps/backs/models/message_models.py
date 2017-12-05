#coding: utf-8
from django.contrib.auth.models import User
from django.db import models


# 发货方式
class Message(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # 用户
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True) #时间
    
    def __unicode__(self):
        return self.title
