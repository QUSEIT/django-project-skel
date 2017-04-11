#coding:utf-8
"""生产运营表单"""
import datetime
from django import forms
from django.forms.utils import ErrorList
from django.forms.extras.widgets import SelectDateWidget


class OperateInfoForm(forms.Form):
    project = forms.CharField(label="项目名称",widget=forms.TextInput(attrs={'class':'form-control required',
                                                            'placeholder': '项目名称',
                                                            'required':'required'}),
                              error_messages={'required': '*请输入项目名称'})

    address = forms.CharField(label="项目地址",widget=forms.TextInput(attrs={'class':'form-control required',
                                                            'placeholder': '项目地址',
                                                            'required':'required'}),
                              error_messages={'required': '*请输入项目地址'})

    start_date = forms.DateField(label="计划开工日期",
                               widget=forms.DateInput(attrs={"placeholder": "计划开工日期(格式如2017-01-01)",
                                                             "class": "form-control required",
                                                             "pattern": "^\d{4}(\-|\/|\.)\d{1,2}(\-|\/|\.)\d{1,2}$",
                                                             'required':'required'}))

    finish_date = forms.DateField(label="计划竣工日期",
                                  widget=forms.DateInput(attrs={"placeholder": "计划竣工日期(格式如2017-01-01)",
                                                                "class": "form-control required",
                                                                "pattern": "^\d{4}(\-|\/|\.)\d{1,2}(\-|\/|\.)\d{1,2}$",
                                                                'required':'required'}))

    content = forms.CharField(label="项目概述",
                              widget=forms.Textarea(attrs={'rows': 3,
                                                           'class':'form-control required',
                                                           "placeholder": "项目简要内容及工程量",
                                                           'required': 'required'}),
                              error_messages={'required': '*请输入项目简要内容及工程量'})

    condition_content = forms.CharField(label="需备条件",
                                        widget=forms.Textarea(attrs={'rows': 3,
                                                                     'class':'form-control required',
                                                                     "placeholder": "服务单位需具备条件",
                                                                     'required': 'required'}),
                                        error_messages={'required': '*请输入服务单位需具备条件'})

    contacts = forms.CharField(label="联系人",
                               widget=forms.TextInput(attrs={'class':'form-control required',
                                                             'placeholder': '联系人',
                                                             'required':'required'}),
                               error_messages={'required': '*请输入联系人'})

    linkman_job = forms.CharField(label="职务", widget=forms.TextInput(attrs={'class':'form-control required',
                                                                'placeholder': '职务',
                                                                'required':'required'}),
                                  error_messages={'required': '*请输入职务'})

    phone = forms.CharField(label="联系方式", widget=forms.TextInput(attrs={'class':'form-control required',
                                                          'placeholder': '联系方式(手机号码)',
                                                          'required':'required',
                                                          "pattern":"(13\d|14[57]|15[^4,\D]|17[678]|18\d)\d{8}|170[059]\d{7}"}),
                              error_messages={'required': '*请输入联系方式(手机号码)',
                                              'invalid': '*请输入有效的手机格式'})