from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request

from django.db import models 


class UserPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: GenericAPIView) -> bool:
        if view.action == "create":
            return True  # anyone can create user, no additional checks needed.
        if view.action == "list":
            return request.user.is_authenticated and request.user.is_staff
        elif view.action in ["retrieve", "update", "partial_update", "destroy"]:
            return True  # defer to has_object_permission
        else:
            return False

    def has_object_permission(
        self, request: Request, view: GenericAPIView, obj: models.Model
    ) -> bool:
        if not request.user.is_authenticated:
            return False

        if view.action in ["retrieve", "update", "partial_update", "destroy"]:
            return obj == request.user or request.user.is_staff
        else:
            return False
