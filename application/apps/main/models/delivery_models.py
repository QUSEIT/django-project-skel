#coding: utf-8
from django.db import models


# 发货方式
class DeliveryWay(models.Model):
    name = models.CharField(max_length=20)  # 名称
    price = models.IntegerField(help_text=u'单位是便士')  # 价格
    logo = models.CharField(max_length=200, blank=True)  # 图片
    type = models.CharField(max_length=20) #时间， 选择或查看仓库地址
    show = models.BooleanField(default=1)  #是否显示出来，1为显示  0 为隐藏
    type2 = models.CharField(max_length=5, default='self')  # self 使用天天的服务， other 使用第三方服务(self 按次数算邮费，other按包裹数量或重量算邮费)

    def __unicode__(self):
        return self.name