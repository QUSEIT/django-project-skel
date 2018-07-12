#coding: utf-8
from django import forms
from django.forms.utils import ErrorList


class GoodsForm(forms.Form):
    #物资表单
    goods_name = forms.CharField(label='物资名称',
                                 widget=forms.TextInput(attrs={'class': 'span6 form-control required'}),
                                 error_messages={'required': '*请输入物资名称'})
    
    goods_number = forms.CharField(label='物资编码',
                                   widget=forms.TextInput(attrs={'class':'span6 form-control required'}),
                                   error_messages={'required': '*请输入物资编码'})

    price = forms.CharField(label='物资价格',
                            widget=forms.NumberInput(attrs={'class':'span6 form-control required'}),
                            error_messages={'required': '*请输入物资价格'})

    stock = forms.CharField(label='库存',
                            widget=forms.NumberInput(attrs={'class':'span6 form-control required'}),
                            error_messages={'required': '*请输入物资库存'})

    goods_type = forms.ChoiceField(choices=(),label='选择类型',
                                   widget=forms.Select(attrs={'class':'span6 form-control'}))

    producers = forms.ChoiceField(choices=(),label='选择厂商',
                                  widget=forms.Select(attrs={'class':'span6 form-control'}))

    is_lease = forms.CharField(label='出租',
                               required = False,
                               widget=forms.CheckboxInput(attrs={'class':'checked'}))

    image1 = forms.ImageField(label='物资图片',
                             widget=forms.FileInput(attrs={'class':''}),
                             error_messages={'required': '*请选择图片'})

    image2 = forms.ImageField(label='物资图片',
                             widget=forms.FileInput(attrs={'class':''}),
                             error_messages={'required': '*请选择图片'})

    image3 = forms.ImageField(label='物资图片',
                             widget=forms.FileInput(attrs={'class':''}),
                             error_messages={'required': '*请选择图片'})

    def __init__(self, type_data=None, producers_data=None, *args, **kwargs):
        super(GoodsForm, self).__init__(*args, **kwargs)
        if type_data:
            self.fields['goods_type'].choices = type_data

        if producers_data:
            self.fields['producers'].choices = producers_data
