#coding: utf-8
from django.contrib import admin
from .models.message_models import Message

admin.site.register(Message)