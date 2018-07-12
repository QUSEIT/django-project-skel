#coding: utf-8
from django.core.cache import cache
from apps.settings import LOGIN_URL
from django.shortcuts import redirect
import urllib
from apps.api.utils import generate_token

def login_required():
    #登录验证
    def wrap(view_func):
        def is_login(self, *args, **kwargs):
            token = self.request.session.get('token', None)
            self.user_id = self.request.session.get('user_id', None)
            
            if not self.user_id or token != generate_token(self.user_id):
                url = LOGIN_URL
                if self.request.path.count("next") > 3:
                    return redirect(url)
                if "?" not in url:
                    get_method_param_keys = self.request.GET.keys()
                    if get_method_param_keys:
                        data = {}
                        #get GET params
                        for key in get_method_param_keys:
                            data[key] = self.request.GET.get('%s' % key)

                        _next = self.request.path + "?" + urllib.urlencode(data)
                        
                        url += "?" + urllib.urlencode(dict(next=_next))
                    else:
                        url += "?" + urllib.urlencode(dict(next=self.request.path))
                return redirect(url)
            return view_func(self, *args, **kwargs)
        return is_login
    return wrap
