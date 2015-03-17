from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bcrobot.views.home', name='home'),
    # url(r'^out','bcrobot.views.out',name='out'),
    #production usage
    url(r'^outcome','bearychat.views.outcome',name='outcome'),
    url(r'^ingo','bearychat.views.ingo',name='ingo'),
    url(r'^weixin','weixin.views.weixin'),
    #hackernews
    url(r'hn','hacknews.views.hn'),
    url(r'^admin/', include(admin.site.urls)),
)
