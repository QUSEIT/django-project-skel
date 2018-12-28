#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from apps.models.user_models import SystemUser
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from datetime import datetime


class SimpleContentForm(forms.Form):
    title = forms.CharField(label='标题',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入标题'})

    content = forms.CharField(label='内容',
                              required = False,
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*请输入内容'})


class SystemUserForm(forms.Form):
    ROLE = ((1, '管理员'), (0, '审核员'),(2, '内容管理员'),)

    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control'}))
    permission = forms.ChoiceField(choices= ROLE,label='权限',
        widget=forms.Select(attrs={'class':'form-control'})
    )
    nickname = forms.CharField(label='昵称', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_username(self):
        cd = self.cleaned_data
        username = cd.get('username')
        user = User.objects.filter(username=username)
        if user.count():
            raise forms.ValidationError("*用户名已经存在")
        return username

    def clean_password(self):
        cd = self.cleaned_data
        password = cd.get('password')
        if len(password)<6 or len(password) > 20:
            raise forms.ValidationError("*请输入6-20位长度密码")
        return password

    def clean_confirm_password(self):
        cd = self.cleaned_data
        confirm_password = cd.get("confirm_password")
        password = cd.get("password")
        if confirm_password <> password:
            raise forms.ValidationError("*两次密码不一致")
        return confirm_password

    def save(self):
        username = self.cleaned_data.get("username")
        nickname = self.cleaned_data.get("nickname")
        password = self.cleaned_data.get("password")
        permission = self.cleaned_data.get("permission")
        user = User.objects.create_user(username=username,
                                        password=password,
                                        last_login=datetime.now(),
                                        is_active = True)
        user.save
        sys_user = SystemUser.objects.create(user=user,
                                             nickname=nickname,
                                             role = permission)
        return user

class SetPasswordForm(forms.Form):
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class':'form-control'}),
                               error_messages={'required': '*请输入6-20位长度密码'})
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                       error_messages={'required': '*请输入6-20位长度密码'})

    def clean_password(self):
        cd = self.cleaned_data
        password = cd.get('password')
        if len(password)<6 or len(password) > 20:
            raise forms.ValidationError("*请输入6-20位长度密码")
        return password

    def clean_confirm_password(self):
        cd = self.cleaned_data
        confirm_password = cd.get("confirm_password")
        password = cd.get("password")
        if confirm_password <> password:
            raise forms.ValidationError("*两次密码不一致")
        return confirm_password

    def save(self, username):
        oldpassword = self.cleaned_data.get("oldpassword")
        password = self.cleaned_data.get("password")
        user = User.objects.get(username=username)
        if user:
            user.set_password(password)
            user.save()
            return user
