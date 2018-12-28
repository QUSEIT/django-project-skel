#coding:utf-8
from django import forms
from django.forms.utils import ErrorList


class WangEditor(forms.Form):
    content = forms.CharField(label='详细介绍',
                              required = False,
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}))