#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from hacknews.hnapi import HackerNewsAPI

# Create your views here.
import json
import requests

def hn(request):
    cmd=''
    bcdata = json.loads(request.body)
    print bcdata
    print bcdata['text'], bcdata['user_name'], bcdata['trigger_word'], bcdata['token'], bcdata['ts'], bcdata[
        'channel_name']
    message = u'输入有误，bcrobot help继续操作'
    print type(bcdata['text'])
    api=HackerNewsAPI()
    stories=[]
    cmd=bcdata['text'].split()
    if len(cmd)>1:
        cmd=cmd[1]
    else:
        cmd=''
    if cmd == "top":
        stories = api.getTopStories(extra_page=1)
    elif cmd == "newest":
        stories = api.getNewestStories(extra_page=1)
    elif cmd == "best":
        stories = api.getBestStories(extra_page=1)
    elif cmd=='help':
        message = u'hacknews <top newest best> 三选一'
    message=""
    for item in stories:
        mess="["+item.title+"]("+item.URL+")  "
        message+=mess
    if message!="":
        message="HackerNews  "+message
        message+=u"订阅hacknews推送服务可获得更好体验"
    else:
        message="No HackerNews found"
    data = {"text": message, "markdown": True,
            "attachments": [{"title": "", "text": "Cool! Attachments supported in Outcoming robot please inform matrix.orz@gmail.com to support bcrobot", "color": "#ffa500"}]}
    return HttpResponse(json.dumps(data))


