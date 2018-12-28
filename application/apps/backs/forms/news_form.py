#coding:utf-8
from django import forms
from django.forms.utils import ErrorList
from apps.models.news_models import NewsType, NewsInfo

class NewsContentForm(forms.Form):
    title = forms.CharField(label='标题',
                            widget=forms.TextInput(attrs={'class':'form-control'}),
                            error_messages={'required': '*请输入资讯标题'})

    news_type = forms.ChoiceField(choices=(),label='资讯类型',
                                   widget=forms.Select(attrs={'class':'form-control'}))

    content = forms.CharField(label='资讯内容', 
                              widget=forms.Textarea(attrs={'id':'wangeditor',"class": "large m-wrap"}),
                              error_messages={'required': '*资讯内容为必填项'})

    preview = forms.ChoiceField(label='是否预览',
                                widget=forms.RadioSelect(attrs={'class': 'radio','default': 1}),
                                choices=((1, u'预览'), (0, u'直接发布')))
    
    def __init__(self, chioce_data=None, *args, **kwargs):
        super(NewsContentForm, self).__init__(*args, **kwargs)
        if chioce_data:
            self.fields['news_type'].choices = chioce_data

    def save(self, status=True, author=0):
        title = self.cleaned_data.get("title")
        news_type = self.cleaned_data.get("news_type")
        content = self.cleaned_data.get("content")
        news_type = NewsType.objects.get(id=int(news_type))
        news_info =  NewsInfo.objects.create(news_type = news_type,
                                             title = title,
                                             status = status,
                                             author = author,
                                             content = content)

        return news_info
    def edit(self, newsid, title, newstype, content, status=True):
        NewsInfo.objects.filter(id=int(newsid)).update(title = title,
                                                       news_type=newstype,
                                                       content=content,
                                                       status=status)