#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from apps.models.goods_models import GoodsType2, GoodsType, GoodsAttr,\
                                     GoodsAttrTemplate, GoodsAttrSet,\
                                     GoodsProducers

class GoodsTypeForm(forms.Form):
    title = forms.CharField(label='名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入名称'})

class GoodsType2Form(forms.Form):
    #2级类别
    title = forms.CharField(label='类别',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入类别名称'})

    goods_type = forms.ChoiceField(choices=(),label='所属类型',
                                   widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self, chioce_data=None, *args, **kwargs):
        super(GoodsType2Form, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['goods_type'].choices = chioce_data


    def save(self):
        title = self.cleaned_data.get("title")
        goods_type = self.cleaned_data.get("goods_type")
        goods_type = GoodsType.objects.get(id=int(goods_type))
        _info =  GoodsType2.objects.create(goods_type=goods_type, title=title)
        return _info

class GoodsAttrForm(forms.Form):
    #属性
    key = forms.CharField(label='key',
                          widget=forms.TextInput(attrs={'class':'form-control'}),
                          error_messages={'required': '*请输入识别该字段的字母或单词'})

    title = forms.CharField(label='属性',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入属性名称'})
    def save(self):
        title = self.cleaned_data.get("title")
        key = self.cleaned_data.get("key")
        _info =  GoodsAttr.objects.create(key=key, title=title)
        return _info

class AttrTemplateForm(forms.Form):
    #属性模版
    title = forms.ChoiceField(choices=(),label='选择属性',
                              widget=forms.Select(attrs={'class':'form-control'}))

    def __init__(self, chioce_data=None, *args, **kwargs):
        super(AttrTemplateForm, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['title'].choices = chioce_data


class AddAttrTemplate(forms.Form):
    #添加模版
    title = forms.CharField(label='模版名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入模版名称'})

class GoodsForm(forms.Form):
    #物资表单
    goods_name = forms.CharField(label='物资名称',
                                 widget=forms.TextInput(attrs={'class':'form-control form-control required'}),
                                 error_messages={'required': '*请输入物资名称'})

    goods_number = forms.CharField(label='物资编码',
                                 widget=forms.TextInput(attrs={'class':'form-control form-control'}),
                                 error_messages={'required': '*请输入物资编码'})

    goods_format = forms.CharField(label='规格型号',
                                 widget=forms.TextInput(attrs={'class':'form-control form-control required'}),
                                 error_messages={'required': '*请输入规格型号'})

    zhuangtai  = forms.CharField(label='状态（新/修复件）',
                                 required=False,
                                 widget=forms.TextInput(attrs={'class':'form-control form-control'}))

    price = forms.CharField(label='物资价格',
                            widget=forms.NumberInput(attrs={'class':'form-control form-control required'}),
                            error_messages={'required': '*请输入物资价格'})

    stock = forms.CharField(label='库存',
                            widget=forms.NumberInput(attrs={'class':'form-control form-control required'}),
                            error_messages={'required': '*请输入物资库存'})

    goods_type2 = forms.ChoiceField(choices=(),label='选择类型',
                                   widget=forms.Select(attrs={'class':'form-control form-control'}))

    goods_type3 = forms.ChoiceField(choices=(),label='主机型号',
                                    widget=forms.Select(attrs={'class':'form-control form-control'}))

    producers = forms.ChoiceField(choices=(),label='品牌',
                                  widget=forms.Select(attrs={'class':'form-control form-control'}))


    def __init__(self, type_data=None, producers_data=None, type3_data=None,*args, **kwargs):
        super(GoodsForm, self).__init__(*args, **kwargs)
        if type_data:
            self.fields['goods_type2'].choices = type_data

        if producers_data:
            self.fields['producers'].choices = producers_data

        if type3_data:
            self.fields['goods_type3'].choices = type3_data

class AddGoodsShelfForm(forms.Form):
    #货架
    title = forms.CharField(label='货架名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入货架名称'})
