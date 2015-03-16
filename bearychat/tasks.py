import  requests
# from django.conf import settings
# from celery import Celery
# BROKER='redis://127.0.0.1:6379/1'
# celery=Celery('tasks',broker=BROKER)
from celeryconfig import celery
from bcrobot import settings


@celery.task(name="app.tasks.add")
def add(x, y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z

@celery.task
def publish(message):
    payload={"text":message,"attachments":[{"title":"Star Wars III","text":"Return of the Jedi","color":"#ffa500"}]}
    headers = {'content=type': 'application/json'}
    r=requests.post(settings.BC_WEBHOOK,json=payload,headers=headers)
    if r.ok:
        return True
    else:
        return False
    # data = {"payload": '{"text":"notify from celery"}'}
    # session = requests.Session()
    # r2 = session.post(url=settings.BC_WEBHOOK, data=data)
    # if r2.ok:
    #     return True
    # else:
    #     return False

@celery.task
def server_report():
    message='Server is OK'
    publish(message)