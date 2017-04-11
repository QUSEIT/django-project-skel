#coding:utf-8
from django import forms
from django.forms.utils import ErrorList

class RecruitForm(forms.Form):
    #招聘表单
    title = forms.CharField(label='招聘岗位',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入招聘岗位'})

    pay = forms.CharField(label='待遇',
                          widget=forms.TextInput(attrs={'class':'form-control'}),
                          error_messages={'required': '*请输入提供待遇'})

    diplomas = forms.CharField(label='文凭要求',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入文凭要求'})

    experience = forms.CharField(label='经验要求',
                                 widget=forms.TextInput(attrs={'class':'form-control'}),
                                 error_messages={'required': '*请输入经验要求'})

    people = forms.CharField(label='招聘人数',
                             widget=forms.TextInput(attrs={'class':'form-control'}),
                             error_messages={'required': '*请输入招聘人数'})

    company = forms.CharField(label='招聘单位',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入招聘单位'})

    address = forms.CharField(label='工作地址',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入工作地址'})

    contacts = forms.CharField(label='联系人',
                               widget=forms.TextInput(attrs={'class':'form-control'}),
                               error_messages={'required': '*请输入联系人'})

    phone = forms.CharField(label='联系方式',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入联系方式'})

    email = forms.CharField(label='email',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入email'})

    is_agent = forms.CharField(label='是否代理招聘',
                               required = False,
                               widget=forms.CheckboxInput(attrs={'class':'checked'}))

    content = forms.CharField(label='详细介绍',
                              required = False,
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}))