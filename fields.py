# apps/{{ app_name }}/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import {{ app_name | capfirst }}
from .serializers import {{ app_name | capfirst }}Serializer


# Create your serializers here.
class {{ app_name | capfirst }}Field(PrimaryKeyRelatedField):
    queryset = {{ app_name | capfirst }}.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = {{ app_name | capfirst }}Serializer(instance)
        return serializer.data
