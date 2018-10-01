# apps/core/schemas.py
# Python imports


# Django imports


# Third party apps imports
import graphene


# Local imports
from apps.authentication.schemas import (
    AuthMutation, GroupQuery, GroupMutation, UserQuery,)


# Create your schemas here.
class Query(GroupQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(GroupMutation, AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
