# config/settings/develop.py
import os

from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS_TESTING = (
    'django_extensions',
    'speedinfo',
)

INSTALLED_APPS += THIRD_PARTY_APPS_TESTING

# Django Rest Framework CORS configuration
CORS_ORIGIN_ALLOW_ALL = True

# Graph models conf
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
    'output': 'database.png',
    'exclude_models': ','.join([
        'AbstractBaseSession',
        'AbstractUser',
        'ContentType',
        'Group',
        'LogEntry',
        'Permission',
        'Session',
        'Token',
    ])
}

# Django Speedinfo conf
MIDDLEWARE += [
    'speedinfo.middleware.ProfilerMiddleware',
]

CACHES = {
    'default': {
        'BACKEND': 'speedinfo.backends.proxy_cache',
        'CACHE_BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
