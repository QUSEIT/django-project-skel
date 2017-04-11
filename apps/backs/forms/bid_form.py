#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from apps.models.bid_models import BidType, BidInfo, BidKnowledge,\
                                   BidKnowledgeType
from libs.qiniu_api import Uploader


class BidTypeForm(forms.Form):
    title = forms.CharField(label='标题',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入招标类型名称'})

    def save(self):
        title = self.cleaned_data.get('title')
        bid_type = BidType.objects.create(title=title)
        return bid_type


class BidInfoForm(forms.Form):
    title = forms.CharField(label='项目名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入项目名称'})

    url = forms.CharField(label='项目地址',
                          widget=forms.TextInput(attrs={'class':'form-control'}),
                          error_messages={'required': '*请输入项目地址'})

    bid_type = forms.ChoiceField(choices=(),label='类型')

    bid_file = forms.FileField(label='招标文件(选填)',
                              required=False,
                              error_messages={'required': '*招标文件为必填项'})

    # 投标截止时间待补充

    content = forms.CharField(label='详细说明',
                              required=False,
                              widget=forms.Textarea(attrs={'id':'wangeditor',
                              'class': 'large m-wrap'}))

    status = forms.BooleanField(label='直接发布',
                                required = False,
                                widget=forms.CheckboxInput(attrs={'class':\
                                'checked'}))

    def __init__(self, chioce_data=None, *args, **kwargs):
        super(BidInfoForm, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['bid_type'].choices = chioce_data

    def save(self):
        file_data = self.cleaned_data.get('bid_file')
        about_file = ''
        if file_data:
            about_file = Uploader().save_file_to_qiniu(file_data)
        bid_type = self.cleaned_data.get('bid_type')
        user_id = 0# 表明是系统发布
        title = self.cleaned_data.get('title')
        url = self.cleaned_data.get('url')
        content = self.cleaned_data.get('content')
        if content == None:
            content = ''
        status = self.cleaned_data.get('status')
        bid_type = BidType.objects.get(id=int(bid_type))
        bid_info = BidInfo.objects.create(bid_type=bid_type,
                                            user_id=user_id,
                                            title=title,
                                            content=content,
                                            url=url,
                                            status=status,
                                            about_file=about_file)
        return bid_info


class BidKnowledgeTypeForm(forms.Form):
    title = forms.CharField(label='标题',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入招标知识类型名称'})

    def save(self):
        title = self.cleaned_data.get('title')
        bidknowledge_type = BidKnowledgeType.objects.create(title=title)
        return bidknowledge_type
        

class BidKnowledgeForm(forms.Form):
    title = forms.CharField(label='标题',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入项目名称'})

    bidknowledge_type = forms.ChoiceField(choices=(),
                                          label='类型',
                                          widget=forms.Select(attrs={'class':'form-control'}),)

    content = forms.CharField(label='详细说明',
                                widget=forms.Textarea(attrs={'id':'wangeditor',
                                'class': 'large m-wrap'}),
                                error_messages={'required': '*请输入详细说明'})

    status = forms.BooleanField(label='直接发布',
                                required = False,
                                widget=forms.CheckboxInput(attrs={'class':\
                                'checked'}))

    def __init__(self, chioce_data=None, *args, **kwargs):
        super(BidKnowledgeForm, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['bidknowledge_type'].choices = chioce_data

    """
    forum = forms.BooleanField(label='发布到论坛',
                                required = False,
                                widget=forms.CheckboxInput(attrs={'class':\
                                'checked'}))
    """

    def save(self):
        bidknowledge_type = self.cleaned_data.get('bidknowledge_type')
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        status = self.cleaned_data.get('status')
        bidknowledge_type = BidKnowledgeType.objects.get(id=int(bidknowledge_type))
        bid_knowledge = BidKnowledge.objects.create(bidknowledge_type=bidknowledge_type,
                                                    title=title,
                                                    content=content,
                                                    status=status)
        return bid_knowledge
