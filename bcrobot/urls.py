from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bcrobot.views.home', name='home'),
    url(r'^out','bcrobot.views.out',name='out'),
    url(r'^outcome','bearychat.views.outcome',name='outcome'),
    url(r'^ingo','bearychat.views.ingo',name='ingo'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$','test.views.index'),
    # url(r'^outgoing','test.views.outgoing'),
    url(r'^weixin','weixin.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
