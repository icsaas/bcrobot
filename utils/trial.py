#-*- coding: utf-8 -*-
import  requests
import  os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bcrobot.settings")
from django.conf import settings
payload={"text":"##caohai  ##hedan  [link](http://lab.justpic.org)","markdown":"true",
         "attachments":[
    {"title":"123","text":"[justtest](http://lab.justpic.org)","color":"#ffa500"},
    {"title":"Title2","text":"![justtest2](http://ww4.sinaimg.cn/bmiddle/ebce0648jw1eq2vzmsyboj21w02iokjm.jpg)  [justtest3](http://cqu.edu.cn)","color":"#ffa500"},
    ]}
headers = {'content=type': 'application/json'}
r=requests.post(settings.BC_WEBHOOK,json=payload,headers=headers)
print r