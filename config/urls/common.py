# Python imports


# Django imports
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


# Third party apps imports
from graphene_django.views import GraphQLView


# Local imports
from apps.core.views import GraphQLViewWithStatusCodes
from apps.authentication.middlewares import TokenAuthenticationMiddleware


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphiql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('graphql/', csrf_exempt(GraphQLViewWithStatusCodes.as_view(
        middleware=[TokenAuthenticationMiddleware]))),
    path('api/', csrf_exempt(GraphQLViewWithStatusCodes.as_view(
        middleware=[TokenAuthenticationMiddleware]))),
]
