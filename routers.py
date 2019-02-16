# apps/{{ app_name }}/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import {{ app_name | capfirst cut:" " }}ViewSet


# Create your routers here.
{{ app_name }} = (
    (r'{{ app_name | capfirst cut:" " }}', {{ app_name | capfirst cut:" " }}ViewSet),
)
