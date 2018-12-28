#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from apps.api.conf import DIMENSION_RATION_CHOICE
from apps.models.ad_models import AdPageInfo


class AdPostionForm(forms.Form):
    #广告位
    def ChioceData():
        return tuple(DIMENSION_RATION_CHOICE)

    title = forms.CharField(label='广告位',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入广告位'})

    size = forms.ChoiceField(choices= ChioceData(),label='选择尺寸(宽x高)',
                             widget=forms.Select(attrs={'class':'form-control'}))

    count = forms.CharField(label='广告位图片数量',
                            widget=forms.NumberInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入广告位图片数量'})

    def clean_count(self):
        cd = self.cleaned_data
        count = cd.get('count')

        if not int(count) >= 1:
            raise forms.ValidationError("*请输入有效的广告位图片数量(大于等于1)")
        return count

"""
class AdInfoForm(forms.Form):
    #广告信息

    
    link = forms.URLField(label='广告链接',
                          widget=forms.TextInput(attrs={'class':'form-control'}),
                          error_messages={'required': '*请输入广告链接'}) 

    
    img = forms.ImageField(label='广告图片',
                           error_messages={'required': '*请选择广告图片'})
    point = forms.CharField(label='显示顺序',
                            widget=forms.NumberInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入显示顺序'})
"""