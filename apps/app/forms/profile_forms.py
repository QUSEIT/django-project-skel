#coding:utf-8
"""用户表达"""
from django import forms
from django.forms.utils import ErrorList

class ProfileResume(forms.Form):
    #个人简历
    name = forms.CharField(label='姓名',
                           widget=forms.TextInput(attrs={'class':'form-control',
                                                         'placeholder': '姓名',
                                                         }),
                           error_messages={'required': '*请输入姓名'})

    sex = forms.ChoiceField(label='性别',
                            widget=forms.RadioSelect(attrs={'class': 'radio','default': 1}),
                            choices=((1, u'男'), (0, u'女')))

    age = forms.CharField(label='年龄',
                           widget=forms.TextInput(attrs={'class':'form-control',
                                                         'placeholder': '年龄',
                                                         }),
                           error_messages={'required': '*请输入年龄'})

    phone = forms.CharField(label='联系方式',
                            widget=forms.TextInput(attrs={'class':'form-control',
                                                          'placeholder': '联系方式',
                                                          "pattern": "(13\d|14[57]|15[^4,\D]|17[678]|18\d)\d{8}|170[059]\d{7}"}),
                            error_messages={'required': '*请输入联系方式',
                                            'invalid': '*请输入有效的手机格式'})

    email = forms.EmailField(label='邮箱',
                             widget=forms.TextInput(attrs={'class':'form-control',
                                                           'placeholder': '邮箱'}),
                             error_messages={'required': '*请输入邮箱',
                                             'invalid': '*请输入有效的邮箱格式'})

    edu_back = forms.CharField(label='学历',
                               widget=forms.TextInput(attrs={'class':'form-control',
                                                             'placeholder': '学历'}),
                               error_messages={'required': '*请输入学历'})

    experience = forms.CharField(label='工作经验',
                                 widget=forms.Textarea(attrs={'class':'form-control',
                                                              'rows': "5",
                                                              'placeholder': '工作经验'}),
                                 error_messages={'required': '*请输入工作经验'})
    
    self_valuation = forms.CharField(label='自我介绍',
                                     widget=forms.Textarea(attrs={'class':'form-control', 
                                                                  'rows': "5",
                                                                  'placeholder': '自我介绍'}),
                                     error_messages={'required': '*请输入自我介绍'})    