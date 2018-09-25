# Python imports


# Django imports


# Third party apps imports
import graphene


# Local imports
from core.schemas.group import Query as GroupQuery, Mutation as GroupMutation
from core.schemas.user import Query as UserQuery
from core.schemas.auth import Mutation as AuthMutation


# Create your schemas here.
class Query(GroupQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(GroupMutation, AuthMutation, graphene.ObjectType):
    pass
