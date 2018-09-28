# Python imports


# Django imports


# Third party apps imports
import graphene


# Local imports
from apps.core.schemas.group import Query, Mutation
from apps.core.schemas.user import Query as UserQuery
from apps.core.schemas.auth import Mutation as AuthMutation


# Create your schemas here.
class Query(GroupQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(GroupMutation, AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
