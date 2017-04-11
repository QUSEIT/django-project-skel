#coding:utf-8
"""专业技术表单"""
from django import forms
from django.forms.utils import ErrorList
from apps.models.tech_models import TechType, TechnicalService

class TechTypeForm(forms.Form):
    title = forms.CharField(label='类型',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入类型名称'})

    image = forms.FileField(label='图片',
                            error_messages={'required': '*请选择图片'})

    content = forms.CharField(label='描述',
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*描述为必填项'})

class TechContentForm(forms.Form):
    
    title = forms.CharField(label='业务',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入业务名称'})

    tech_type = forms.ChoiceField(choices=(),label='业务类型',
                                   widget=forms.Select(attrs={'class':'form-control'}))

    content = forms.CharField(label='内容', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*业务介绍为必填项'})

    preview = forms.BooleanField(label='是否预览',
                                 required = False,
                                 widget=forms.CheckboxInput(attrs={'class':'checked'}))
    
    def __init__(self, chioce_data=None, *args, **kwargs):
        super(TechContentForm, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['tech_type'].choices = chioce_data
    
    def save(self, status=True):
        title = self.cleaned_data.get("title")
        tech_type = self.cleaned_data.get("tech_type")
        content = self.cleaned_data.get("content")
        tech_type = TechType.objects.get(id=int(tech_type))
        tech_info =  TechnicalService.objects.create(type_id=tech_type,
                                                    title=title,
                                                    status=status,
                                                    content=content)

        return tech_info

class TechCaseForm(forms.Form):
    title = forms.CharField(label='案例简介',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入简介'})

    about_file = forms.FileField(label='文件（图片或视频）')

    is_video = forms.CharField(label='视频',
                               required = False,
                               widget=forms.CheckboxInput(attrs={'class':'checked'}))

    content = forms.CharField(label='详细介绍', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*请输入详细介绍'})