#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from libs.qiniu_api import Uploader

class ZhongchuangForm(forms.Form):
    name = forms.CharField(label='公司名称',
                            widget=forms.TextInput(attrs={'class':'span6',
                                                          'class':'form-control',
                                                          'placeholder': '公司名称',
                                                          'id':'name',}),
                            error_messages={'required': '*请输入公司名称'})
    
    linkman = forms.CharField(label='联系人',
                          widget=forms.TextInput(attrs={'class': 'span6',
                                                        'class':'form-control',
                                                        'placeholder': '联系人',
                                                        'id':'linkman',}),
                          error_messages={'required': '*请输入联系人'})

    phone = forms.CharField(label='联系方式(手机号码)',
                          widget=forms.TextInput(attrs={'class': 'span6',
                                                        'class': 'form-control',
                                                        'id': 'phone',
                                                        'placeholder': '联系方式(手机号码)',
                                                        'pattern':'(13\d|14[57]|15[^4,\D]|17[678]|18\d)\d{8}|170[059]\d{7}'}),
                          error_messages={'required': '*请输入联系方式',
                                          'invalid': '*请输入有效的手机格式'})
    
    money = forms.CharField(label='金额',
                            widget=forms.TextInput(attrs={'class':'span6',
                                                          'class':'form-control',
                                                          'id':'money','placeholder': '金额'}),
                            error_messages={'required': '*请输入金额'})
    
    content = forms.CharField(label='说明',
                          widget=forms.Textarea(attrs={'class':'span6',
                                                       'class':'form-control',
                                                       'id':'content',
                                                       'placeholder': '说明',
                                                       'rows':'5'}),
                          error_messages={'required': '*请输入说明'})
    
    
class ZhongbaoForm(forms.Form):
    name = forms.CharField(label='公司名称',
                            widget=forms.TextInput(attrs={'class':'span6',
                                                          'class':'form-control',
                                                          'placeholder': '公司名称',
                                                          'id':'name',}),
                            error_messages={'required': '*请输入公司名称'})
    
    linkman = forms.CharField(label='联系人',
                          widget=forms.TextInput(attrs={'class':'span6',
                                                        'class':'form-control',
                                                        'placeholder': '联系人',
                                                        'id': 'linkman'}),
                          error_messages={'required': '*请输入联系人'})

    phone = forms.CharField(label='联系方式(手机号码)',
                          widget=forms.TextInput(attrs={'class':'span6',
                                                        'class':'form-control',
                                                        'id':'phone',
                                                        'placeholder': '联系方式(手机号码)',
                                                        'pattern':'(13\d|14[57]|15[^4,\D]|17[678]|18\d)\d{8}|170[059]\d{7}'}),
                          error_messages={'required': '*请输入联系方式',
                                          'invalid': '*请输入有效的手机格式'})
    
    money = forms.CharField(label='金额',
                          widget=forms.TextInput(attrs={'class':'span6',
                                                        'class':'form-control',
                                                        'id':'money',
                                                        'placeholder': '金额',}),
                          error_messages={'required': '*请输入金额'})
    
    content = forms.CharField(label='说明',
                          widget=forms.Textarea(attrs={'class': 'span6',
                                                       'class': 'form-control',
                                                       'id': 'content',
                                                       'placeholder': '说明',
                                                       'rows': '5'}),
                          error_messages={'required': '*请输入说明'})
    