# Python imports


# Django imports
from django.contrib.auth import models as auth_models


# Third party apps imports
import graphene
from graphene_django.types import DjangoObjectType


# Local imports
from apps.core.utils import model_filter


# Create your schemas here.
class UserWhereUniqueInput(graphene.InputObjectType):
    id = graphene.ID()


class UserWhereInput(UserWhereUniqueInput):
    AND = graphene.Field('apps.authentication.schemas.UserWhereInput')
    OR = graphene.Field('apps.authentication.schemas.UserWhereInput')
    email = graphene.String()


class User(DjangoObjectType):
    class Meta:
        model = auth_models.User


class UserQuery(graphene.ObjectType):
    users = graphene.List(User, where=UserWhereInput())
    user = graphene.Field(User, where=UserWhereUniqueInput(required=True))

    def resolve_users(self, info, where=None):
        return model_filter(auth_models.User.objects.all(), where)

    def resolve_user(self, info, where):
        users = model_filter(auth_models.User.objects.all(), where)
        assert len(users) < 2, 'Many Users found'
        assert len(users) > 0, 'User not found'
        return users.first()
