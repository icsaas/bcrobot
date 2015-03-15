"""
Django settings for bcrobot project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from config import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import sys

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4d0#&50kh$i&3fb^wwp*3hhq33*zp$(hno1^a1f)*83-oe25(r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bearychat',
    'weixin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bcrobot.urls'

WSGI_APPLICATION = 'bcrobot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
ENV=''
try:
    import sae.const
    ENV='SAE'
except Exception,e:
    ENV='LOCAL'

if ENV=='SAE':
    DATABASES={
        'default':{
            'ENGINE':'django.db.backends.mysql',
            'NAME':sae.const.MYSQL_DB,
            'USER':sae.const.MYSQL_USER,
            'PASSWORD':sae.const.MYSQL_HOST,
            'PORT':sae.const.MYSQL_PORT
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

PROJECT_ROOT = os.path.dirname(
    os.path.abspath(sys.modules[os.environ['DJANGO_SETTINGS_MODULE']].__file__)
  )

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, '../templates'),
    os.path.join(PROJECT_ROOT,'../decorators/templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #   'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ( 'django.core.context_processors.static',
                                'django.core.context_processors.media',
                                'django.contrib.auth.context_processors.auth',
                                'django.core.context_processors.request',    )