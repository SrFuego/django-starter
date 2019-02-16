# apps/{{ app_name }}/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import {{ app_name | capfirst }}


# Register your models here.
@admin.register({{ app_name | capfirst }})
class {{ app_name | capfirst }}ModelAdmin(admin.ModelAdmin):
    pass
