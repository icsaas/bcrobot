# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from bearychat.models import Subscribe
import requests
import json

#trial for bearychat InComing Robot
# Create your views here.
def ingo(request):
    #method1 post json to the server
    # payload={"text":"caohai123","attachments":[{"title":"Star Wars III","text":"Return of the Jedi","color":"#ffa500"}]}
    # headers = {'content=type': 'application/json'}
    # r=requests.post(settings.BC_WEBHOOK,json=payload,headers=headers)
    #method2 post payload form data to server
    data = {"payload": '{"text":"haha"}'}
    session = requests.Session()
    r2 = session.post(url=settings.BC_WEBHOOK, data=data)
    print r2
    if r2.ok:
        return render_to_response("index.html")

#trial for bearychat OutComing Robot
@csrf_exempt
def outcome(request):
    bcdata=json.loads(request.body)
    print bcdata
    print bcdata['text'],bcdata['user_name'],bcdata['trigger_word'],bcdata['token'],bcdata['ts'],bcdata['channel_name']
    message='输入有误，请输入justpic help继续操作'
    if bcdata['text'].startswith('justpic'):
        cmd=str(bcdata['text']).split()
        if cmd[1]=='sub':
            #store the bearychat room info: subscribe info
            if cmd[2] is not None:
                sub=Subscribe()
                sub.username=bcdata['user_name']
                sub.channel=bcdata['channel_name']
                sub.url=cmd[2]
                sub.save()
            else:
                message='请重新输入，不支持该操作！'
        elif cmd[1]=='cancel':
            bcdata['user_name'],bcdata['channel_name']
            pass
        elif cmd[1]=='wx':
            pass
        elif cmd[1]=='tianqi':
            pass
        elif cmd[1]=='help':
            message='help'
        else:
            message='输入有误，请输入justpic help继续操作'

    elif bcdata['text'].startswith('history'):
        pass
    else:
        pass
    data = {'text': "text, this field may accept markdown",'attachments': [{'title': "title_1",'text': "attachment_text",'color': "#ffffff",}]}
    return HttpResponse(json.dumps(data))
