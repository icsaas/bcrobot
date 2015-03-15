# -*- coding: utf-8 -*-
from django.utils.encoding import smart_str
from django.shortcuts import render_to_response
from xml.etree import ElementTree as etree
from django.http import HttpResponse
from django.conf import  settings
import hashlib



class weixin_required:
    """此装饰类，将数据读入，传递字典，并将装饰函数的返回字典组装成xml"""

    def __init__(self,other):
        self.other = other
        self.db()

    def db(self):
        #文本消息
        text = ('ToUserName','FromUserName','CreateTime','MsgType','Content','MsgId')
        image = ('ToUserName','FromUserName','CreateTime','Msgtype','PicUrl','MediaId','MsgId')
        voice = ('ToUserName','FromUserName','CreateTime','Msgtype','MediaId','Fromat','MsgId')
        video = ('ToUserName','FromUserName','CreateTime','Msgtype','MediaId','ThumbMediaId','MsgId')
        location = ('ToUserName','FromUserName','CreateTime','Msgtype','Location_X','Location_Y','Scale','Label','MsgId')
        link = ('ToUserName','FromUserName','CreateTime','Msgtype','Title','Description','Url','MsgId')
        music = None
        news = None

        #总消息
        self.TYPE = {
            'text':(text,'text.xml'),
            'image':(image,'image.xml'),
            'voice':(voice,'voice.xml'),
            'video':(video,'video.xml'),
            'music':(music,'music.xml'),
            'news':(news,'news.xml'),
        }

    def __call__(self,request):
        #服务器验证
        if request.method=='GET':
            token = settings.WEIXIN_TOKEN
            yanzhen_list = [
                request.GET.get('timestamp',None),
                request.GET.get('nonce',None),
                token,
            ]
            yanzhen_list.sort()
            yanzhen_xinxi = "%s%s%s" % tuple(yanzhen_list)
            yanzhen_xinxi = hashlib.sha1(yanzhen_xinxi).hexdigest()
            if yanzhen_xinxi == request.GET.get('signature',None):
                return HttpResponse(request.GET.get('echostr',None))
            else:
                return None

        #数据格式化处理
        xml_str = smart_str(request.body)
        xml = etree.fromstring(xml_str)

        #通过定义的字典将数据读取出来
        xiaoxi_list,xml_dir = self.TYPE[xml.find('MsgType').text]
        xiaoxi = {}
        for x in xiaoxi_list:
            try:
                xiaoxi[x] = xml.find(x).text
            except:
                xiaoxi[x] = xml.find(x)

        #调用处理消息的函数/类
        xiaoxi = self.other(xiaoxi)

        #返回渲染并插入好的网页
        xiaoxi_list,XML_dir = self.TYPE[xiaoxi['MsgType']]
        return render_to_response(XML_dir, xiaoxi)
