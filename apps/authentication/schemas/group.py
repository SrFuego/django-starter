# Python imports


# Django imports
from django.contrib.auth import models as auth_models
from django.db.transaction import atomic


# Third party apps imports
import graphene
from graphene_django.types import DjangoObjectType


# Local imports
from apps.core.utils import model_filter
from .permission import PermissionManyInput, connect_group


# Create your schemas here.
class GroupWhereUniqueInput(graphene.InputObjectType):
    id = graphene.ID()


class GroupWhereInput(GroupWhereUniqueInput):
    AND = graphene.Field('apps.authentication.schemas.GroupWhereInput')
    OR = graphene.Field('apps.authentication.schemas.GroupWhereInput')
    name = graphene.String()


class Group(DjangoObjectType):
    class Meta:
        model = auth_models.Group


class GroupQuery(graphene.ObjectType):
    groups = graphene.List(Group, where=GroupWhereInput())
    group = graphene.Field(Group, where=GroupWhereUniqueInput(required=True))

    def resolve_groups(self, info, where=None):
        return model_filter(auth_models.Group.objects.all(), where)

    def resolve_group(self, info, where):
        groups = model_filter(auth_models.Group.objects.all(), where)
        assert len(groups) < 2, 'Many Groups found.'
        assert len(groups) > 0, 'Group not found'
        return groups.first()


class GroupCreateInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    permissions = PermissionManyInput()


class GroupUpdateInput(graphene.InputObjectType):
    name = graphene.String()
    permissions = PermissionManyInput()


class OutputGroup(graphene.ObjectType):
    Output = Group


class CreateGroup(OutputGroup, graphene.Mutation):
    class Arguments:
        data = GroupCreateInput(required=True)

    @atomic
    def mutate(self, info, data):
        group = auth_models.Group()
        group.name = data.name
        group.save()

        connect_group(group, info, data)

        return group


class UpdateGroup(OutputGroup, graphene.Mutation):
    class Arguments:
        data = GroupUpdateInput(required=True)
        where = GroupWhereUniqueInput(required=True)

    @atomic
    def mutate(self, info, data, where):
        group = GroupQuery().resolve_group(info, where)

        if data.get('name'):
            group.name = data.name

        group.save()

        connect_group(group, info, data)

        return group


class DeleteGroup(OutputGroup, graphene.Mutation):
    class Arguments:
        where = GroupWhereUniqueInput(required=True)

    def mutate(self, info, where):
        group = GroupQuery().resolve_group(info, where)
        group.delete()
        return group


class GroupMutation(graphene.ObjectType):
    create_group = CreateGroup.Field()
    update_group = UpdateGroup.Field()
    delete_group = DeleteGroup.Field()
