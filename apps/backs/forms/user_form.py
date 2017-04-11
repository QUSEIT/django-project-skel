#coding:utf-8
"""用户表单"""
from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.models import User



class UpdataPasswordForm(forms.Form):
    password = forms.CharField(label='新密码',
                               widget=forms.PasswordInput(attrs={'class':'form-control1',
                                                                 'required':'required'}),
                               error_messages={'required': '*请输入新密码'})

    confirm_password = forms.CharField(label='确认密码',
                               widget=forms.PasswordInput(attrs={'class':'form-control1',
                                                                 'required':'required'}),
                               error_messages={'required': '*请输入确认密码'})

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