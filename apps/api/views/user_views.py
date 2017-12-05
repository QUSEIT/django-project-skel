#--*--coding:utf-8--*--
from apps.backs.views.base_views import BaseHandler
from django.contrib.auth.models import User


class UserList(BaseHandler):
    def get(self, request):
        data = {
            'list': list(range(10)),
            'data': {
                'icon': list(range(20))
            },
            'user': list(User.objects.filter().values('username', 'email', 'is_active', 'is_superuser'))
        }
        return self.write_json({'errno': 0, 'msg': 'success', 'data': data})
