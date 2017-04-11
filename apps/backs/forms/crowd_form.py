#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
import datetime

class ZhongChuangForm(forms.Form):
    #众创表单
    title = forms.CharField(label='项目名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入项目名称'})

    finishdate = forms.DateField(label='截止日期',
                               initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class':'form-control'}),
                               error_messages={'required': '*请输入截止日期'})

    company = forms.CharField(label='发起单位',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*单位名称'})

    contacts = forms.CharField(label='联系人',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入联系人'})
    phone = forms.CharField(label='联系方式',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入联系方式'})

    money = forms.CharField(label='预算',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入预算'})

    about_file = forms.FileField(label='项目文件(选填)',
                                 required=False)

    content = forms.CharField(label='详细介绍',
                              required = False,
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}))

    
class ZhongBaoForm(forms.Form):
    #众包表单
    title = forms.CharField(label='项目名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入项目名称'})
    
    finishdate = forms.DateField(label='截止日期',
                               initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class':'form-control'}),
                               error_messages={'required': '*请输入截止日期'})

    company = forms.CharField(label='发起单位',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*单位名称'})
    
    contacts = forms.CharField(label='联系人',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入联系人'})
    phone = forms.CharField(label='联系方式',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入联系方式'})

    money = forms.CharField(label='预算',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入预算'})

    address = forms.CharField(label='项目地址',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入项目地址'})

    about_file = forms.FileField(label='项目文件(选填)',
                                 required=False)

    content = forms.CharField(label='详细介绍',
                              required = False,
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}))