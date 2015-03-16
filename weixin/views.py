#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from decorators.weixin import weixin_required
from weixin.models import User,Message,New
# Create your views here.

#user processor
def user(request):
    """store user info，return user status"""
    return_user = {}
    return_user['FromUserName'] = request['FromUserName']
    return_user['CreateTime'] = request['CreateTime']

    # update user info
    for i in User.objects.all():
        if request['FromUserName'] == i.FromUserName:
            return_user['zhuangtai'] = i.zhuangtai
            return_user['zhuangtai_ma'] = i.zhuangtai_ma
            return_user['zhuangtai_time'] = i.zhuangtai_time
            return_user['id'] = i.id
            return return_user

    # 如果没有查找到 返回 -1
    return -1

def user_update(request):
    """store new user"""
    try:
        u = User(
            id = request['id'],
            FromUserName = request['FromUserName'],
            CreateTime = request['CreateTime'],
            zhuangtai = request['zhuangtai'],
            zhuangtai_ma = request['zhuangtai_ma'],
            zhuangtai_time = request['zhuangtai_time']
        )
    except:
        u = User(
            FromUserName = request['FromUserName'],
            CreateTime = request['CreateTime'],
            zhuangtai = request['zhuangtai'],
            zhuangtai_ma = request['zhuangtai_ma'],
            zhuangtai_time = request['zhuangtai_time']
        )
    u.save()

def news(request,meiyegeshu,dijiye):
    meiyegeshu = int(meiyegeshu)+1
    dijiye = int(dijiye)
    if dijiye < 1:
        return -1

    return_news = {}
    return_news['ToUserName'] = request['FromUserName']
    return_news['FromUserName'] = request['ToUserName']
    return_news['CreateTime'] = request['CreateTime']
    return_news['MsgType'] = 'news'

    #返回字典页
    weixin_news = New.objects.all()
    weixin_news_long = len(weixin_news)
    if meiyegeshu*(dijiye-1) < weixin_news_long:
        weixin_news = New.objects.all()[meiyegeshu*(dijiye-1):meiyegeshu*dijiye]
    else:
        return -1

    return_news['ArticleCount'] = int(len(weixin_news))
    return_news['Articles'] = new_Articles(weixin_news)
    return return_news

def new_Articles(new_classs):
    """传入元组，将其中的类实力变成列表返回"""
    Articles = ()
    for articles in new_classs:
        Articles += (new_Article(articles),)
    return Articles

def new_Article(new_class):
    """将new类传入，返回new的字典"""
    Article = {}
    Article['Title'] = new_class.Title
    Article['Description'] = new_class.Description
    Article['PicUrl'] = new_class.PicUrl
    Article['Url'] = new_class.Url
    return Article

def index(request):
    pass

@csrf_exempt
@weixin_required
def weixin(request):
    # 常量定义
    print request
    home_help = {
        'FromUserName':request['ToUserName'],
        'ToUserName':request['FromUserName'],
        'CreateTime':request['CreateTime'],
        'MsgType':'text',
        'Content':'''欢迎关注JustPic微信
回复：
    1 进入justpic菜单
    help 查看帮助
其他功能我们正在开发ing'''
    }
    lishitueisong_help = {
        'FromUserName':request['ToUserName'],
        'ToUserName':request['FromUserName'],
        'CreateTime':request['CreateTime'],
        'MsgType':'text',
        'Content':'''回复：
    1 上一页
    2 下一页
    3 退出justpic菜单'''
    }
    lishitueisong_error = {
        'FromUserName':request['ToUserName'],
        'ToUserName':request['FromUserName'],
        'CreateTime':request['CreateTime'],
        'MsgType':'text',
        'Content':'''你浏览的页面不存在
回复：
    1 上一页
    2 下一页
    3 退出JustPic菜单'''
    }

    # 先判断用户是否有保存的信息

    # 如果是新用户，返回帮助
    re_user = user(request)
    if re_user == -1:
        re_user = {
            'FromUserName':request['FromUserName'],
            'CreateTime':request['CreateTime'],
            'zhuangtai':'home',
            'zhuangtai_ma':'',
            'zhuangtai_time':request['CreateTime']
        }
        user_update(re_user)

        xiaoxi = home_help
        return xiaoxi
    else:
        # 判断时间是否超时
        pass

    # 对状态和消息判断需要返回信息
    if re_user['zhuangtai'] == 'home':
        if request['Content'] == '1':
            re_user['zhuangtai'] = 'lishitueisong'
            re_user['zhuangtai_ma'] = '1'

            xiaoxi = news(request,10,1)
        else:
            xiaoxi = home_help

    # 历史推送状态判断
    elif re_user['zhuangtai'] == 'lishitueisong':
        xiaoxi = lishitueisong_help
        if request['Content'] == '1':
            yema = int(re_user['zhuangtai_ma'])
            yema -=1
            re_user['zhuangtai_ma'] = str(yema)
            xiaoxi = news(request,10,yema)
            if xiaoxi == -1:
                xiaoxi = lishitueisong_error

        elif request['Content'] == '2':
            yema = int(re_user['zhuangtai_ma'])
            yema +=1
            re_user['zhuangtai_ma'] = str(yema)
            xiaoxi = news(request,10,yema)
            if xiaoxi == -1:
                xiaoxi = lishitueisong_error

        elif request['Content'] in ['help','3']:
            re_user['zhuangtai'] = 'home'
            re_user['zhuangtai_ma'] = ''
            xiaoxi = home_help

    user_update(re_user)
    return xiaoxi

