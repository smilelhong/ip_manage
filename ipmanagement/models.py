# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
# Create your models here.
class IP_Address(models.Model):
    ip = models.GenericIPAddressField(verbose_name=u"IP地址")
    gateway = models.GenericIPAddressField(verbose_name=u"网关")
    network = models.GenericIPAddressField(verbose_name=u"网络号")
    netmask = models.CharField(max_length=20,default='',null=True,blank='',verbose_name=u"掩码")
    system = models.CharField(max_length=64,default='',null=True,blank='',verbose_name=u"应用系统")
    apply_person = models.CharField(max_length=64,default='',null=True,blank='',verbose_name=u"申请人")
    state = models.CharField(max_length=20,choices=((u"已分配",u"已分配"),(u"未分配",u"未分配")),verbose_name=u"状态")
    apply_time = models.DateField(default=datetime.now(),verbose_name=u"申请时间")

class IP_Range(models.Model):
    start_ip = models.GenericIPAddressField(verbose_name=u"开始IP")
    end_ip = models.GenericIPAddressField(verbose_name=u"结束IP")
    network = models.GenericIPAddressField(verbose_name=u"网络号")
    netmask = models.CharField(max_length=20,default='',verbose_name=u"掩码")
    use_ip = models.CharField(max_length=20,default='',null=True,blank='',verbose_name=u"已使用IP数")
    left_ip = models.CharField(max_length=20,default='',null=True,blank='',verbose_name=u"未使用IP数")
    create_time = models.DateField(default=datetime.now(),verbose_name=u"创建时间")
    des = models.CharField(max_length=20,default='',null=True,blank='',verbose_name=u"描述")