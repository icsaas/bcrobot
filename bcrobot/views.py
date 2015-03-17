from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
import requests
import json

#trial for bearychat InComing Robot
# Create your views here.
def home(request):
    #method1 post json to the server
    payload={"text":"caohai123","attachments":[{"title":"Star Wars III","text":"Return of the Jedi","color":"#ffa500"}]}
    headers = {'content=type': 'application/json'}
    r=requests.post(settings.BC_WEBHOOK,json=payload,headers=headers)
    if r.ok:
        return render_to_response('index.html')
    #method2 post payload form data to server
    # data = {"payload": '{"text":"haha"}'}
    # session = requests.Session()
    # r2 = session.post(url=settings.BC_WEBHOOK, data=data)
    # print r2
    # if r2.ok:
    #     return render_to_response("index.html")

#trial for bearychat OutComing Robot
@csrf_exempt
def out(request):
    bcdata=json.loads(request.body)
    print bcdata
    print bcdata['text'],bcdata['user_name'],bcdata['trigger_word'],bcdata['token'],bcdata['ts'],bcdata['channel_name']
    if request.POST:
        print 'post'
    data = {'text': "text, this field may accept markdown",'attachments': [{'title': "title_1",'text': "attachment_text",'color': "#ffffff",}]}
    return HttpResponse(json.dumps(data))
