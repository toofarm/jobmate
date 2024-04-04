from django.urls import path
from rest_framework.routers import format_suffix_patterns
from .views import UserViewSet

urlpatterns = [
    path(
        "users/",
        UserViewSet.as_view({"get": "list", "post": "create"}),
        name="user-list",
    ),
    path(
        "users/<int:pk>/",
        UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="user-detail",
    ),
    path(
        "users/create/",
        UserViewSet.as_view({"post": "create"}),
        name="user-create",
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
