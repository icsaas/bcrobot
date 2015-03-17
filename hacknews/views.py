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
    message = '输入有误，bcrobot help继续操作'
    print type(bcdata['text'])
    api=HackerNewsAPI()
    stories=[]
    if cmd == "top":
        stories = api.getTopStories(extra_page=1)
    elif cmd == "newest":
        stories = api.getNewestStories(extra_page=1)
    elif cmd == "best":
        stories = api.getBestStories(extra_page=1)
    message=""
    for item in stories:
        mess="["+item.title+"]("+item.URL+")  "
        message+=mess
    if message!="":
        message="HackerNews  "+message
    else:
        message="No HackerNews found"
    data = {"text": message, "markdown": True,
            "attachments": [{"title": "", "text": "Cool,Attachments supported in Outcoming robot", "color": "#ffa500"}]}
    return HttpResponse(json.dumps(data))


