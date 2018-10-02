# apps/core/views.py
# Python imports


# Django imports


# Third party apps imports
from graphene_django.views import GraphQLView
from graphql.error import GraphQLLocatedError


# Local imports


# Create your views here.
class GraphQLViewWithStatusCodes(GraphQLView):
    @staticmethod
    def format_error(error):
        formatted_error = GraphQLView.format_error(error)

        if isinstance(error, GraphQLLocatedError):
            original_error = error.original_error
            code = getattr(original_error, 'status_code', None)

            if code:
                formatted_error['code'] = code

        return formatted_error