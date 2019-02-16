# apps/{{ app_name }}/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import {{ app_name | capfirst }}


# Create your serializers here.
class {{ app_name | capfirst }}Serializer(ModelSerializer):

    class Meta:
        model = {{ app_name | capfirst }}
        fields = '__all__'
