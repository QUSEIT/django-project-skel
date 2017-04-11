#-*-coding:utf8;-*-
"""base views"""
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.cache import cache
import logging
import json
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from apps.settings import PAGE_LIMIT




class BaseHandler(View):
    #基础类，公共函数
    PAGE_LIMIT =  PAGE_LIMIT
    API_MSG_SIZE = "?imageView2/0/w/480/h/480"

    
    def get_cache_user_info(self, user_id):
        """用户缓存信息"""
        if user_id:
            user_info = cache.get('UserInfo:%s' % user_id)
            if not user_info:
                user_info = UserInfo.objects.filter(id=user_id)
                if len(user_info):
                    user_info = user_info[0]
                    d = {"nickname": user_info.nickname,
                         "avatar": user_info.avatar or 'http://o7tb2rscn.bkt.clouddn.com/avatar/default.jpg',
                         "device_id": user_info.device_id,
                         "phone": user_info.phone}
                    cache.set('UserInfo:%s' % user_id, json.dumps(d))
                    return d
            else:
                return json.loads(cache.get('UserInfo:%s' % user_id))

        return {}

    def delete_cache_user_info(self, user_id):
        """清除用户缓存信息"""
        cache.delete("UserInfo:%s" % user_id)


    def write_json(self, obj):
        """return json obj"""
        return HttpResponse(json.dumps(obj, indent=4, sort_keys=False, ensure_ascii=False), content_type='application/json')
