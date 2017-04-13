#coding: utf-8
from django.core.cache import cache
from apps.settings import BACKS_LOGIN_URL
from django.shortcuts import redirect
import urllib
from apps.api.utils import backs_token


def login():
    #后台登录验证
    def wrap(view_func):
        def is_login(self, *args, **kwargs):
            token = self.request.session.get('backs_token', None)
            self.user = self.request.user
            self.username = self.request.session.get('backs_username', None)
            self.user_id = self.request.session.get('backs_user_id', None)

            if not self.user_id or token != backs_token(self.user_id) or not self.user:
                url = BACKS_LOGIN_URL
                if self.request.path.count("next") > 3:
                    return redirect(url)
                if "?" not in url:
                    url += "?" + urllib.urlencode(dict(next=self.request.path))
                return redirect(url)
            return view_func(self, *args, **kwargs)
        return is_login
    return wrap
