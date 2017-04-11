
#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from apps.models.bid_models import BidType, BidInfo, BidKnowledge,\
                                   BidKnowledgeType, BiddingInfo
from libs.qiniu_api import Uploader


class BidInfoForm(forms.Form):
    def ChioceData():
        data = []
        for item in BidType.objects.filter(is_delete=False):
            data.append([item.id, item.title])
        return tuple(data)

    title = forms.CharField(label='项目名称',
                            widget=forms.TextInput(attrs={'class':'span6'}),
                            error_messages={'required': '*请输入项目名称'})

    url = forms.CharField(label='项目地址',
                          widget=forms.TextInput(attrs={'class':'span6'}),
                          error_messages={'required': '*请输入项目地址'})

    bid_type = forms.ChoiceField(choices= ChioceData(),label='类型')

    bid_file = forms.FileField(label='招标文件',
                               error_messages={'required': '*招标文件为必填项'})

    # 投标截止时间待补充

    content = forms.CharField(label='详细说明',
                              required=False,
                              widget=forms.Textarea(attrs={'id':'wangeditor',
                              'class': 'large m-wrap'}))

    def save(self, user_id):
        file_data = self.cleaned_data.get('bid_file')
        about_file = Uploader().save_file_to_qiniu(file_data)
        bid_type = self.cleaned_data.get('bid_type')
        title = self.cleaned_data.get('title')
        url = self.cleaned_data.get('url')
        content = self.cleaned_data.get('content')
        print user_id
        if content == None:
            content = ''
        bid_type = BidType.objects.get(id=int(bid_type))
        bid_info = BidInfo.objects.create(bid_type=bid_type,
                                            user_id=user_id,
                                            title=title,
                                            content=content,
                                            url=url,
                                            about_file=about_file)
        return bid_info


class BiddingForm(forms.Form):
    name = forms.CharField(label='公司名称',
                            widget=forms.TextInput(attrs={'class':'span6','class':'form-control','placeholder': '公司名称','required':'required'}),
                            error_messages={'required': '*请输入公司名称'})
   
    linkman = forms.CharField(label='联系人',
                          widget=forms.TextInput(attrs={'class':'span6','class':'form-control', 'placeholder': '联系人','required':'required'}),
                          error_messages={'required': '*请输入联系人'})

    phone = forms.CharField(label='联系方式(手机号码)',
                          widget=forms.TextInput(attrs={'class':'span6',
                                                        'class':'form-control',
                                                        'placeholder': '联系方式(手机号码)',
                                                        'required':'required',
                                                        'pattern':'(13\d|14[57]|15[^4,\D]|17[678]|18\d)\d{8}|170[059]\d{7}'}),
                          error_messages={'required': '*请输入联系方式',
                                          'invalid': '*请输入有效的手机格式'})
    
    bidding_file = forms.FileField(label='竞标文件',
                                   widget=forms.TextInput(attrs={'type': 'file',
                                                                 'style':'float:left;width:50%;margin-bottom: 10px',
                                                                 'placeholder': '竞标文件',
                                                                 'required':'required',
                                                                 'pattern':'True',
                                                                 'id':"bidding_file",
                                                                 "name":"bidding_file"}),
                                   error_messages={'required': '*竞标文件为必填项'})
    
    def save(self, user_id, bid_id):
        file_data = self.cleaned_data.get('bidding_file')
        about_file = Uploader().save_file_to_qiniu(file_data)
        name = self.cleaned_data.get('name')
        code = self.cleaned_data.get('code')
        linkman = self.cleaned_data.get('linkman')
        phone = self.cleaned_data.get('phone')
        bidding_info = BiddingInfo.objects.create(bid_id=bid_id,
                                                  user_id=user_id,
                                                  name=name,
                                                  code=code,
                                                  linkman=linkman,
                                                  phone=phone,
                                                  about_file=about_file)
        return bidding_info
