#--*--coding:utf-8--*--
from apps.backs.views.base_views import BaseHandler
from apps.api.logger import logger_decorator


class Example(BaseHandler):
    @logger_decorator
    def get(self, request):
        data = {
            'list': map(lambda x: x * 2, range(10)),
            'filter_data': filter(lambda x: x % 2 ==1, range(10)),
            'data': {
                'icon': None
            }
        }
        return self.write_json({'errno': 0, 'msg': 'success', 'data': data})
