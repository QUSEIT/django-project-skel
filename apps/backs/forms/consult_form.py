#coding:utf-8
"""咨询服务"""
from django import forms
from django.forms.utils import ErrorList
from apps.models.hr_models import Consultation

class ConsultForm(forms.Form):    

    
    title = forms.CharField(label='标题',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入标题'})

    content = forms.CharField(label='咨询服务内容', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*咨询服务内容为必填项'})

    preview = forms.CharField(label='预览',
                              required = False,
                              widget=forms.CheckboxInput(attrs={'class':'checked'}))
    
    def save(self, status=True):
        title = self.cleaned_data.get("title")
        news_type = self.cleaned_data.get("news_type")
        content = self.cleaned_data.get("content")
        news_info = Consultation.objects.create(title = title,
                                                status = status,
                                                content = content)

        return news_info

    def edit(self, title, content):
        Consultation.objects.filter(id=int(newsid)).update(title = title,
                                                           content=content)