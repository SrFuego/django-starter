# config/settings/develop.py
import os

from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS_LOCAL = (
    'django_extensions',
    'speedinfo',
)

INSTALLED_APPS += THIRD_PARTY_APPS_LOCAL

# Django Rest Framework CORS configuration
CORS_ORIGIN_ALLOW_ALL = True

# Graph models conf
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
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
