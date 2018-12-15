# config/settings/develop.py
import os

from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Django Rest Framework CORS configuration
CORS_ORIGIN_ALLOW_ALL = True
