from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bcrobot.views.home', name='home'),
    # url(r'^out','bcrobot.views.out',name='out'),
    #production usage
    url(r'^outcome','bcstart.views.outcome',name='outcome'),
    url(r'^ingo','bcstart.views.ingo',name='ingo'),
    url(r'^weixin','weixin.views.weixin',name='weixin'),
    #hackernews
    url(r'hn','hacknews.views.hn',name='hackernews'),
    url(r'chat','chat.views.index',name='chat'),
    url(r'^admin/', include(admin.site.urls)),
)
