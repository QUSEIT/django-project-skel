#coding:utf-8
"""教材"""
from django import forms
from django.forms.utils import ErrorList



class TeachMetaForm(forms.Form):
    #教材表单
    title = forms.CharField(label='教材名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入教材名称'})
    
    teacher = forms.CharField(label='讲师',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入讲师'})

    about_file = forms.FileField(label='教材文件',
                                 error_messages={'required': '*请选择教材文件'})

    is_video = forms.CharField(label='视频',
                               required = False,
                               widget=forms.CheckboxInput(attrs={'class':'checked'}))

    content = forms.CharField(label='教材介绍', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*请输入教材介绍'})

    """
    price = forms.CharField(label='教材单价',
                            initial = 0,
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入教材单价'})

    inventory = forms.CharField(label='教材库存',
                                widget=forms.TextInput(attrs={'class':'form-control'}),
                                error_messages={'required': '*请输入库存'})
    """