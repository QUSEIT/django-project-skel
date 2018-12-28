#coding:utf-8
"""生产运营表单"""
from django import forms
from django.forms.utils import ErrorList
from apps.models.produ_models import ProduOperaType, ProduOperaInfo

class ProduTypeForm(forms.Form):
    title = forms.CharField(label='类型',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入类型名称'})

    image = forms.FileField(label='图片',
                            error_messages={'required': '*请选择图片'})

    content = forms.CharField(label='描述',
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*描述为必填项'})

class ProduContentForm(forms.Form):
    
    title = forms.CharField(label='业务',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入业务名称'})

    produ_type = forms.ChoiceField(choices=(),label='业务类型',
                                   widget=forms.Select(attrs={'class':'form-control'}))

    content = forms.CharField(label='内容', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*业务介绍为必填项'})

    preview = forms.CharField(label='预览',
                              required = False,
                              widget=forms.CheckboxInput(attrs={'class':'checked'}))

    def __init__(self, chioce_data=None, *args, **kwargs):
        super(ProduContentForm, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['produ_type'].choices = chioce_data
    
    def save(self, status=True):
        title = self.cleaned_data.get("title")
        produ_type = self.cleaned_data.get("produ_type")
        content = self.cleaned_data.get("content")
        produ_type = ProduOperaType.objects.get(id=int(produ_type))
        produ_info =  ProduOperaInfo.objects.create(type_id=produ_type,
                                                    title=title,
                                                    status=status,
                                                    content=content)

        return produ_info

class ProduOperaCaseForm(forms.Form):
    title = forms.CharField(label='案例简介',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入简介'})

    about_file = forms.FileField(label='文件（图片或视频）',
                                 error_messages={'required': '*请选择案例文件（图片或视频）'})

    is_video = forms.CharField(label='视频',
                               required = False,
                               widget=forms.CheckboxInput(attrs={'class':'checked'}))

    content = forms.CharField(label='详细介绍', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*请输入详细介绍'})

class RepairForm(forms.Form):
    title = forms.CharField(label='维修设备',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入维修设备'})

    company = forms.CharField(label='设备所属单位',
                             widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入设备所属单位'})

    contacts = forms.CharField(label='联系人',
                               widget=forms.TextInput(attrs={'class':'form-control'}),
                               error_messages={'required': '*请输入联系人'})

    phone = forms.CharField(label='联系方式',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入联系方式'})

    address = forms.CharField(label='维修地址',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入维修地址'})

    content = forms.CharField(label='维修说明', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*请输入维修说明'})