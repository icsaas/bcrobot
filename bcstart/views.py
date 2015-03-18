# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from bcstart.models import Subscriber
from hacknews.hnapi import HackerNewsAPI
from weixin.models import User, New, Message
from utils.tianqi import weather
import requests
import json
from datetime import datetime
# trial for bearychat InComing Robot
from aiml import TalkBot
bot = TalkBot()

# Create your views here.
def ingo(request):
    # method1 post json to the server
    data = {"text": "Test123",
               "attachments": [{"title": "Star Wars III", "text": "Return of the Jedi", "color": "#ffa500"}]}
    # headers = {'content=type': 'application/json'}
    # r = requests.post(settings.BC_WEBHOOK, json=data, headers=headers)
    r=requests.post(settings.BC_WEBHOOK,data={'payload':json.dumps(data)})

    if r.ok:
        return render_to_response("index.html")

        # method2 post payload form data to server
        # data = {"payload": '{"text":"haha"}'}
        # session = requests.Session()
        # r2 = session.post(url=settings.BC_WEBHOOK, data=data)
        # print r2
        # if r2.ok:
        #     return render_to_response("index.html")


# trial for bearychat OutComing Robot
@csrf_exempt
def outcome(request):
    bcdata = json.loads(request.body)
    message = u'输入有误，bcrobot help继续操作'
    if bcdata['text'].startswith('bcrobot'):
        cmd = bcdata['text'].split()
        if len(cmd) > 1 and cmd[1] == 'sub':
            # store the bearychat room info: subscribe info
            if len(cmd) > 3:
                try:
                    sub = Subscriber.objects.get(username=bcdata['user_name'], channel=bcdata['channel_name'],url=cmd[2],token=bcdata['token'],subtype=cmd[3])
                    if sub is not None:
                        message = u'已订阅推送，请尝试其他操作'
                except Exception, e:
                    sub = Subscriber(
                        username=bcdata['user_name'],
                        channel=bcdata['channel_name'],
                        url=cmd[2],
                        token=bcdata['token'],
                        subtype=cmd[3]
                    )
                    sub.save()
                    message = u'订阅推送成功！'
            else:
                message =u'命令bcrobot sub <incoming url> <subtype>  subtype可为weixin hackernews server weather'
        elif len(cmd) > 1 and cmd[1] == 'cancel':
            if len(cmd) == 2:
                message = u'请指定取消推送消息类型 weixin hackernews server weather'
            else:
                if cmd[2] != 'all':
                    sub = Subscriber.objects.filter(username=bcdata['user_name'], channel=bcdata['channel_name'],
                                                    token=bcdata['token'], subtype=cmd[2])
                else:
                    sub = Subscriber.objects.filter(username=bcdata['user_name'], channel=bcdata['channel_name'],
                                                    token=bcdata['token'])
                if sub == []:
                    message = u"您还没有订阅推送"
                else:
                    sub.delete()
                    message = u'取消推送成功'
        elif len(cmd) > 1 and cmd[1] == 'status':
            try:
                subscribers = Subscriber.objects.filter(username=bcdata['user_name'], channel=bcdata['channel_name'],
                                                    token=bcdata['token'])
                mess=""
                if subscribers==[]:
                    raise Exception
                for item in subscribers:
                    mess+=item.subtype
                    mess+=" "
                message = u'已订阅推送服务 '+mess
            except Exception, e:
                message = u'未订阅推送服务'
        elif len(cmd) > 1 and cmd[1] == 'wx':
            message = u'bcrobot wx users--显示微信关注用户  bcrobot wx news--显示微信推送消息 ' \
                      u'bcrobot wx message <userid>--显示特定用户发送的消息 ' \
                      u'bcrobot wx pub <title> <description> <picurl> <fromurl>--发布微信新闻消息'
            if len(cmd) > 2 and cmd[2] == 'users':
                users = User.objects.all()
                usernames = [item.FromUserName for item in users]
                message = ','.join(usernames) if usernames!=[] else message

            elif len(cmd) > 2 and cmd[2] == 'news':
                news = New.objects.order_by('-Chuangjianshijian')
                i = 0
                mess = ""
                for new in news:
                    if i > 5:
                        break
                    new.Title, new.PicUrl, new.Url, new.Description
                    mess += new.Title + " [![pic](" + new.PicUrl + ")](" + new.Url + ") ;"
                message = mess if mess != "" else message
            elif len(cmd) > 2 and cmd[2] == 'pub':
                try:
                    new = New(
                        Title=cmd[3],
                        Description=cmd[4],
                        PicUrl=cmd[5],
                        Url=cmd[6],
                        Chuangjianshijian=datetime.now())
                    new.save()
                    message = u"新闻发送成功"
                except Exception, e:
                    print e
                    message = u"新闻发送失败，更正后重新发送"
        elif len(cmd) > 1 and cmd[1] == 'weather':
            city = cmd[2] if len(cmd) > 2 else u'重庆'
            message = weather(city)
            message=city+" "+ message
        elif len(cmd)>1 and cmd[1]=='ai':
            message = bot.respond(cmd[2] if len(cmd)>2 else '')

        elif len(cmd)>1 and cmd[1]=='hn':
            option=cmd[2] if len(cmd)>2 else u'best'
            api=HackerNewsAPI()
            stories=[]
            if option == "top":
                stories = api.getTopStories(extra_page=1)
            elif option == "newest":
                stories = api.getNewestStories(extra_page=1)
            elif option == "best":
                stories = api.getBestStories(extra_page=1)
            elif option=='help':
                message = u'bcrobot hn <top newest best> 三选一'
            #拼装消息
            message=""
            for item in stories:
                mess="["+item.title+"]("+item.URL+")  "
                message+=mess
            if message!="":
                message="HackerNews  "+message
                message+=u"受限于attachments，可通过订阅hackernews推送服务可获得更好体验"
            else:
                message=bcdata['user_name']+" "+message

        elif len(cmd) > 1 and cmd[1] == 'help':
            message = u'bcrobot sub <incomgin url> subtype--订阅推送  ' \
                      u'bcrobot cancel--取消订阅推送 ' \
                      u'bcrobot status--查看订阅状态 ' \
                      u'bcrobot wx--微信公众号管理  ' \
                      u'bcrobot weather <city>--天气预报 ' \
                      u'bcrobot hn <best newest top>--HackerNews消息浏览 ' \
                      u'bcrobot ai <message>--AI智能机器人聊天'
        else:
            message = u'输入有误，bcrobot help查看帮助 或者查看https://gitcafe.com/matrixorz/bcrobot 了解详细情况'
    elif 'help' in bcdata['text']:
        message = u'bcrobot sub <incomgin url> subtype--订阅推送  ' \
                  u'bcrobot cancel--取消订阅推送 ' \
                  u'bcrobot status--查看订阅状态 ' \
                  u'bcrobot wx--微信公众号管理  ' \
                  u'bcrobot weather <city>--天气预报 ' \
                  u'bcrobot hn <best newest top>--HackerNews消息浏览 ' \
                  u'bcrobot ai <message>--AI智能机器人聊天'
    else:
        message = u"目前仅支持bcrobot命令，请输入 bcrobot help查看帮助"
    data = {"text": message, "markdown": True,
            "attachments": [{"title": "Notify Developer", "text": "Cool! Attachments supported in Outcoming robot please inform matrix.orz@gmail.com to support bcrobot", "color": "#ffa500"}]}
    # data = {"text": message, "markdown": True,
    # "attachments": [{"title": "Star Wars III", "text": "Return of the Jedi", "color": "#ffa500"}]}
    return HttpResponse(json.dumps(data))
