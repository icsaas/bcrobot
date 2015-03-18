#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=10)
    
class Subscriber(models.Model):
    username=models.CharField(max_length=30,verbose_name=u'订阅者')
    channel=models.CharField(max_length=30,verbose_name=u'订阅通道')
    url=models.CharField(max_length=100,verbose_name=u'webhook地址')
    token=models.CharField(max_length=100,verbose_name=u'Token')
    spacename=models.CharField(max_length=30,verbose_name=u'空间名')
    subtype=models.CharField(max_length=30,verbose_name=u'订阅类型')