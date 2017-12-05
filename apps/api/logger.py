# coding: utf-8
from functools import wraps
import logging
import json
Logger = logging.getLogger(__name__)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def logger_decorator(method):
    """logger 日志记录"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        try:
            json_data = json.loads(self.request.body)
        except Exception as e:
            json_data = {}
        log = {
            'url': self.request.get_full_path(),
            'method': self.request.method,
            'params': self.request.POST.dict() or self.request.GET.dict(),
            'json_data': json_data,
            'is_ajax': self.request.is_ajax(),
            'user': self.request.user.username,
            'ip': get_client_ip(self.request)
        }
        Logger.debug(json.dumps(log))
        return result
    return wrapper
