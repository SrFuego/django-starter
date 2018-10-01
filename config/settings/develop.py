# config/settings/develop.py
import os

from .common import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

THIRD_PARTY_APPS_LOCAL = (
)

INSTALLED_APPS += THIRD_PARTY_APPS_LOCAL


# Snapshottest configuration
TEST_RUNNER = 'snapshottest.django.TestRunner'
