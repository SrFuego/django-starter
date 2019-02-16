# apps/{{ app_name }}/models.py
# Python imports


# Django imports


# Third party apps imports


# Local imports


# Create your models here.
class {{ app_name | capfirst cut:" " }}(models.Model):
    pass

    def __str__(self):
        return str(self.id)