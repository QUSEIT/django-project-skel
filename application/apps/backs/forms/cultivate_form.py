#coding:utf-8
"""培训"""
from django import forms
from django.forms.utils import ErrorList
import datetime
from apps.models.hr_models import TeacherInfo

class TrainingTypeForm(forms.Form):
    title = forms.CharField(label='培训类型名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入培训类型名称'})

    content = forms.CharField(label='描述', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "form-control"}),
                              error_messages={'required': '*请输入描述'})

class TrainingType2Form(forms.Form):
    title = forms.CharField(label='名称',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入名称'})

    attach = forms.FileField(label='资料(选填)',
                             required=False)

    content = forms.CharField(label='描述', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "form-control"}),
                              error_messages={'required': '*请输入描述'})

class CultivateForm(forms.Form):
    title = forms.CharField(label='培训主题',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入培训主题'})

    teacher_id = forms.ChoiceField(label='讲师',
                                   choices= (),
                                   widget=forms.Select(attrs={'class':'chosen form-control', "multiple": "multiple"}))

    start_at = forms.DateField(label='开始培训时间',
                               initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class':'form-control'}),
                               error_messages={'required': '*请输入开始培训时间'})

    student_num = forms.CharField(label='开班人数',
                                  widget=forms.TextInput(attrs={'class':'form-control'}),
                                  error_messages={'required': '*请输入开班人数'})
    
    content = forms.CharField(label='培训内容', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*培训内容为必填项'})

    def __init__(self, chioce_data=None, *args, **kwargs):
        super(CultivateForm, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['teacher_id'].choices = chioce_data


class TeacherForm(forms.Form):
    def ChioceData():
        return tuple((('0', '中级'),
                     ('1', '高级'),
                     ('2', '其他')))

    def chioce_sex():
        return tuple((('女', '女'),
                     ('男', '男')))

    name = forms.CharField(label='姓名',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入姓名'})

    sex = forms.ChoiceField(label='性别',
                            choices= chioce_sex(),
                            widget=forms.Select(attrs={'class':'form-control'}))

    brithday = forms.DateField(label='出生年月',
                               widget=forms.DateInput(attrs={'class':'form-control', "placeholder": '2016-07-08'}),
                               error_messages={'required': '*请输入出生年月',
                                                'invalid': '*请输入有效的时间格式如：2016-07-08'})

    avatar = forms.FileField(label='头像(选填)',
                             required=False)

    company = forms.CharField(label='单位',
                              widget=forms.TextInput(attrs={'class':'form-control'}),
                              error_messages={'required': '*请输入单位'})

    teach_experience = forms.CharField(label='教学经验',
                                       widget=forms.TextInput(attrs={'class':'form-control'}),
                                       error_messages={'required': '*请输入教学经验'})

    master_course = forms.CharField(label='主讲课程',
                                    widget=forms.TextInput(attrs={'class':'form-control'}),
                                    error_messages={'required': '*请输入主讲课程'})

    positions = forms.CharField(label='职位',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入职位'})

    level = forms.ChoiceField(label='职称',
                              choices= ChioceData(),
                              widget=forms.Select(attrs={'class':'form-control'}))

    remarks = forms.CharField(label='备注（选填）',
                              required=False,
                              widget=forms.TextInput(attrs={'class':'form-control'}))

    about_key = forms.CharField(label='关键词（选填）',
                                required=False,
                                widget=forms.TextInput(attrs={'class':'form-control'}),
                            )

    description = forms.CharField(label='人物描述', 
                                  widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                                  error_messages={'required': '*人物描述为必填项'})

class TrainLinkManForm(forms.Form):
    name = forms.CharField(label='姓名',
                           widget=forms.TextInput(attrs={'class':'form-control', "required": "required",}),
                           error_messages={'required': '*请输入姓名'})

    avatar = forms.FileField(label='头像（选填）',required=False)

    phone = forms.CharField(label='联系方式',
                            widget=forms.TextInput(attrs={'class':'form-control',
                                                          "required": "required",
                                                          "pattern":"(13\d|14[57]|15[^4,\D]|17[678]|18\d)\d{8}|170[059]\d{7}"}),
                            error_messages={'required': '*请输入联系方式',
                                            'invalid': '*请输入有效的手机格式'})
    qq = forms.CharField(label='qq',
                         widget=forms.TextInput(attrs={'class':'form-control', "required": "required",}),
                         error_messages={'required': '*请输入qq号'})

    wechat = forms.CharField(label='微信号',
                             widget=forms.TextInput(attrs={'class':'form-control', "required": "required",}),
                             error_messages={'required': '*请输入微信号'})

    email = forms.EmailField(label='邮箱',
                            widget=forms.EmailInput(attrs={'class':'form-control', "required": "required",}),
                            error_messages={'required': '*请输入邮箱'})