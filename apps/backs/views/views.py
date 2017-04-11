#-*-coding:utf8;-*-
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from base_views import BaseHandler
from django.contrib.auth import authenticate

from datetime import datetime
#project
from apps.backs.utils import login
from apps.api.utils import backs_token
#import models
from apps.api.utils import get_client_ip
#import form
from apps.backs.forms.user_form import UpdataPasswordForm


class ManagerLogin(BaseHandler):
    #登录
    NEXT_PATH = "/manager/index" #default backs index
    template_name = 'backs/login.html'
    def get(self, request):
        user_id = request.session.get('backs_user_id', None)
        token = request.session.get('backs_token', None)
        #如果session有效，则跳转到后台首页
        if user_id and token and token == backs_token(user_id):
            self.NEXT_PATH =  self.request.GET.get('next') if bool(self.request.GET.get('next')) else self.NEXT_PATH
            return redirect(self.NEXT_PATH)

        return render(request, self.template_name)

    def post(self, request, template_name='backs/login.html'):
        username = self.request.POST.get("username", None)
        password = self.request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            user.last_login = datetime.now()
            user.save()
            self.request.session["backs_username"] = user.username
            self.request.session["backs_user_id"] = user.id
            self.request.session["backs_token"] = backs_token(user.id)
            self.request.session["backs_role"] = str(1 if user.is_superuser else 0) #权限级别

            #登录记录
            self.NEXT_PATH =  self.request.GET.get('next') if bool(self.request.GET.get('next')) else self.NEXT_PATH
            return redirect(self.NEXT_PATH)
        return render(request,
                      self.template_name)

class ManagerIndex(BaseHandler):
    #首页
    template_name="backs/index.html"
    @login()
    def get(self, request):
        return render(request,
                      self.template_name)

class NotFoundPage(BaseHandler):
    template_name = 'backs/404.html'
    def get(self, request):
        return render(request, self.template_name)

class ManagerLoginOut(BaseHandler):
    def get(self, request):
        request.session.clear()
        print 'aaaaaaaaa'
        return redirect('/manager/login')


class UpdatePassword(BaseHandler):
    """修改密码"""
    template_name = 'backs/form.html'
    page_title = '修改密码'
    @login()
    def get(self, request):
        form = UpdataPasswordForm()
        return render(request, self.template_name, {"form": form, "page_title": self.page_title})

    @login()
    def post(self, request):
        data = request.POST
        form = UpdataPasswordForm(data)
        if form.is_valid():
            data = data.dict()
            form.save(self.username)

            return redirect('/manager/update/password')

        return render(request, self.template_name, {"form": form, "page_title": self.page_title})
