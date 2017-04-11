#coding: utf-8
from apps.models.goods_models import GoodsAttr, GoodsAttrTemplate


class GoodsFormsTemplate(object):
    def generate_form(self, template_id):
        data = []
        attrs = eval(GoodsAttrTemplate.objects.get(id=int(template_id)).attr)
        for item in attrs:
            try:
                attr  = GoodsAttr.objects.get(id=item)
                data.append({"title": attr.title, "key": attr.key})
            except Exception, e:
                continue
        return data



