#--*--coding:utf-8--*--
from apps.backs.views.base_views import BaseHandler


class Example(BaseHandler):
    def get(self, request):
        data = {
            'list': map(lambda x: x * 2, range(10)),
            'filter_data': filter(lambda x: x % 2 ==1, range(10)),
            'data': {
                'icon': None
            }
        }
        return self.write_json({'errno': 0, 'msg': 'success', 'data': data})
