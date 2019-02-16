# apps/{{ app_name }}/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import {{ app_name | capfirst cut:" " }}Serializer
from .models import {{ app_name | capfirst cut:" " }}


# Create your viewsets here.
class {{ app_name | capfirst cut:" " }}ViewSet(ModelViewSet):
    queryset = {{ app_name | capfirst cut:" " }}.objects.all()
    serializer_class = {{ app_name | capfirst cut:" " }}Serializer
