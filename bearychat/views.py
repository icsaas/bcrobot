# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from bearychat.models import Subscribe
from utils.tianqi import  weather
import requests
import json

#trial for bearychat InComing Robot
# Create your views here.
def ingo(request):
    #method1 post json to the server
    payload={"text":"caohai123","attachments":[{"title":"Star Wars III","text":"Return of the Jedi","color":"#ffa500"}]}
    headers = {'content=type': 'application/json'}
    r=requests.post(settings.BC_WEBHOOK,json=payload,headers=headers)
    if r.ok:
        return render_to_response("index.html")

    #method2 post payload form data to server
    # data = {"payload": '{"text":"haha"}'}
    # session = requests.Session()
    # r2 = session.post(url=settings.BC_WEBHOOK, data=data)
    # print r2
    # if r2.ok:
    #     return render_to_response("index.html")

#trial for bearychat OutComing Robot
@csrf_exempt
def outcome(request):
    bcdata=json.loads(request.body)
    print bcdata
    print bcdata['text'],bcdata['user_name'],bcdata['trigger_word'],bcdata['token'],bcdata['ts'],bcdata['channel_name']
    message='输入有误，请输入justpic help继续操作'
    if bcdata['text'].startswith('justpic'):
        cmd=str(bcdata['text']).split()
        if len(cmd)>1 and cmd[1]=='sub':
            #store the bearychat room info: subscribe info
            if len(cmd)>2:
                sub=Subscribe()
                sub.username=bcdata['user_name']
                sub.channel=bcdata['channel_name']
                sub.url=cmd[2]
                sub.save()
                message='订阅推送成功！'
            else:
                message='命令justpic sub <incoming url>！'
        elif len(cmd)>1 and cmd[1]=='cancel':
            Subscribe.objects.filter(username=bcdata['user_name'],channel=bcdata['channel_name']).delete()
        elif len(cmd)>1 and cmd[1]=='wx':
            message='justpic wx users--显示微信关注用户  justpic wx news--显示微信推送消息 justpic wx message <userid>--显示特定用户发送的消息'
            if len(cmd)>2 and cmd[2]=='users':
                pass
        elif len(cmd)>1 and cmd[1]=='tianqi':
            city=cmd[2] if len(cmd)>2 else '重庆'
            print city
            message=weather(city)
        elif len(cmd)>1 and cmd[1]=='help':
            message='justpic sub <incomgin url>--订阅推送  justpic cancel--取消订阅推送  justpic wx--微信公众号信息查看  justpic tianqi <city>--天气预报'
        else:
            message='输入有误，请输入justpic help查看帮助'
    elif 'help' in bcdata['text']:
        message='help message'
    else:
        message="目前仅支持justpic，请输入"+str(bcdata['text'])+" help查看帮助"
    data = {"text": "message","markdown":True,"attachments":[{"title":"Star Wars III","text":"Return of the Jedi","color":"#ffa500"}]}
    return HttpResponse(json.dumps(data))
