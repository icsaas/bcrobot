from django.db import models
from django.db.models.signals import post_save
from django.conf import  settings
import requests
# Create your models here.
class User(models.Model):
    FromUserName = models.CharField(max_length=30,verbose_name='发出消息者')
    CreateTime = models.CharField(max_length=15,verbose_name='消息创建时间')
    zhuangtai = models.CharField(max_length=20,blank=True,null=True,verbose_name='状态')
    zhuangtai_ma = models.CharField(max_length=20,blank=True,null=True,verbose_name='状态码')
    zhuangtai_time = models.CharField(max_length=15,blank=True,null=True,verbose_name='最后状态时间')

def notify_user(sender, instance, created, **kwargs):
    if created:
        headers = {'content=type': 'application/json'}
        data = {"payload": '{"text":"new user"}'}
        session = requests.Session()
        r2 = session.post(url=settings.BC_WEBHOOK, data=data)
        if r2.ok:
            return True
        else:
            return False
        
post_save.connect(notify_user(), sender=User)

class New(models.Model):
    Title = models.CharField(max_length=64,verbose_name='图文标题')
    Description = models.CharField(max_length=120,blank=True,null=True,verbose_name='图文描述')
    PicUrl = models.URLField(verbose_name='图片链接')
    Url = models.URLField(verbose_name='网页链接')
    Chuangjianshijian = models.DateField(verbose_name='图文消息创建时间')

    def __unicode__(self):
        return (self.Title,self.Description)

    class Meta:
        ordering = ['-Chuangjianshijian']

def notify_news(sender, instance, created, **kwargs):
    if created:
        headers = {'content=type': 'application/json'}
        data = {"payload": '{"text":"haha"}'}
        session = requests.Session()
        r2 = session.post(url=settings.BC_WEBHOOK, data=data)
        if r2.ok:
            return True
        else:
            return False

post_save.connect(notify_news(), sender=New)