import os

from django.conf import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bcrobot.settings')

celery = Celery()
celery.config_from_object("celeryconfig")
celery.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')

BROKER_URL = "redis://redis:6379/0"
CELERYD_HIJACK_ROOT_LOGGER = True
CELERY_RESULT_BACKEND = "redis"
CELERY_IMPORTS = ("bearychat.tasks",)
DJANGO_SETTINGS_MODULE = "settings"