from django.shortcuts import render
from hacknews.hnapi import HackerNewsAPI
# Create your views here.
import json
def hn(request):
    cmd=''
    bcdata = json.loads(request.body)
    print bcdata
    print bcdata['text'], bcdata['user_name'], bcdata['trigger_word'], bcdata['token'], bcdata['ts'], bcdata[
        'channel_name']
    message = '输入有误，bcrobot help继续操作'
    print type(bcdata['text'])
    api=HackerNewsAPI()
    if cmd == "top":
        stories = api.getTopStories(extra_page=10)
    elif cmd == "newest":
        stories = api.getNewestStories(extra_page=10)
    elif cmd == "best":
        stories = api.getBestStories(extra_page=10)

