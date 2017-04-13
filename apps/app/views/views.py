#--*--coding:utf-8--*--
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from apps.backs.views.base_views import BaseHandler
# python moduls
import json
import os
import datetime
import time

# project moduls
from apps.api.utils import generate_token, auth_decorator, write_json, \
    generate_password, validate_phone, get_client_ip,\
    get_random_code, separate



class Index(BaseHandler):
    """首页"""
    template_name = 'app/index.html'

    def get(self, request):

        def func():
            for i in ['a', 'b', 'c']:
                yield {i: i}
        return render(request, self.template_name, {'data': func()})

