# apps/{{ app_name }}/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import {{ app_name | capfirst cut:" " }}


# Create your serializers here.
class {{ app_name | capfirst cut:" " }}Serializer(ModelSerializer):

    class Meta:
        model = {{ app_name | capfirst cut:" " }}
        fields = '__all__'
