#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from apps.models.finance_models import FinanceType #, FinanceInfo

class FinanceContentForm(forms.Form):
    title = forms.CharField(label='服务类型',
                            widget=forms.TextInput(attrs={'class':'span6 form-control'}),
                            error_messages={'required': '*请输入服务类型'})

    content = forms.CharField(label='金融服务内容', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*金融服务内容为必填项'})

    preview = forms.BooleanField(label='是否预览',
                                 required = False,
                                 widget=forms.CheckboxInput(attrs={'class':'checked'}))
    
    def save(self, status=True):
        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")
        finance_info =  FinanceType.objects.create(title=title,
                                                   status=status,
                                                   content=content)

        return finance_info
    def edit(self, financeid, title, content):
        info = FinanceType.objects.filter(id=int(financeid)).update(title = title, content=content)
        return info
        
