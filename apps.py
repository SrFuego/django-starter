# apps/{{ app_name }}/apps.py
# Python imports


# Django imports
from django.apps import AppConfig


# Third party apps imports


# Local imports


# Configure your app here.
class {{ app_name | capfirst }}Config(AppConfig):
    name = 'apps.{{ app_name }}'
    verbose_name = '{{ app_name | capfirst }}'
