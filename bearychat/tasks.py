import  requests
# from django.conf import settings
# from celery import Celery
# BROKER='redis://127.0.0.1:6379/1'
# celery=Celery('tasks',broker=BROKER)
from celeryconfig import celery
from bcrobot import settings
from bearychat.models import Subscriber
from hacknews.hnapi import HackerNewsAPI

@celery.task(name="app.tasks.add")
def add(x, y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z

# @celery.task
def publish(message,subtype):
    payload={"text":message,"attachments":[{"title":"服务器运行状况","text":"正常","color":"#ffa500"}]}
    headers = {'content=type': 'application/json'}
    #notify all user
    subscribers=Subscriber.objects.all()
    for item in subscribers:
        r=requests.post(item.url,json=payload,headers=headers )
        print r
        if not r.ok:
            print 'error in publish function'
    #
    # r=requests.post(settings.BC_WEBHOOK,json=payload,headers=headers)
    # if r.ok:
    #     return True
    # else:
    #     return False
    # data = {"payload": '{"text":"notify from celery"}'}
    # session = requests.Session()
    # r2 = session.post(url=settings.BC_WEBHOOK, data=data)
    # if r2.ok:
    #     return True
    # else:
    #     return False

@celery.task
def server_report():
    payload={"text":"来自服务器的消息","attachments":[{"title":"服务器运行状况","text":"正常","color":"#ffa500"}]}
    headers = {'content=type': 'application/json'}
    #notify all user
    subscribers=Subscriber.objects.filter(subtype='server')
    for item in subscribers:
        payload['text']=item.username+" "+payload['text']
        r=requests.post(item.url,json=payload,headers=headers )
        print r
        if not r.ok:
            print 'error in publish function'
    #

@celery.task
def publish_hn():
    api=HackerNewsAPI()
    stories=api.getNewestStories(2)
    attachments=[]
    for item in stories:
        attadict={}
        attadict['title']=item.title
        attadict['text']="["+item.title +"]("+ item.URL+")"
        attadict['color']='#ffa500'
        attachments.append(attadict)

    payload={"text":"HackNews","attachments":attachments}
    headers = {'content=type': 'application/json'}
    #notify all user
    subscribers=Subscriber.objects.filter(subtype='hackernews')
    for item in subscribers:
        payload['text']=item.username+" "+payload['text']
        r=requests.post(item.url,json=payload,headers=headers )
        print r
        if not r.ok:
            print 'error in publish function'

@celery.task
def publish_weather():
    attachments=[]
    payload={"text":"Weather","markdown":True,"attachments":attachments}
    headers = {'content=type': 'application/json'}
    #notify all user
    subscribers=Subscriber.objects.filter(subtype='hackernews')
    for item in subscribers:
        payload['text']=item.username+" "+payload['text']
        r=requests.post(item.url,json=payload,headers=headers )
        print r
        if not r.ok:
            print 'error in publish function'


