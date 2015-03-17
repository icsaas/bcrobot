import os
from celery.schedules import crontab
from django.conf import settings
from celery import Celery
from datetime import  timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bcrobot.settings')

celery = Celery()
celery.config_from_object("celeryconfig")
celery.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')

CELERYBEAT_SCHEDULE = {
    'every-day': {
        'task': 'bearychat.tasks.server_report',
        # 'schedule': timedelta(seconds=10),
        'schedule': crontab(hour='*/12'),
    },
    'every-moments':{
        'task':'bearychat.tasks.publish_hn',
        'schedule':timedelta(minutes=15),
    },
    'every-night':{
        'task':'bearychat.tasks.publish_weather',
        'schedule':crontab(hour='*/24'),
    }
}

BROKER_URL = "redis://localhost:6379/0"
CELERYD_HIJACK_ROOT_LOGGER = True
CELERY_RESULT_BACKEND = "redis"
CELERY_IMPORTS = ("bearychat.tasks",)
DJANGO_SETTINGS_MODULE = "bcrobot.settings"
