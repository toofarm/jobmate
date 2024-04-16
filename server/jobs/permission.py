from rest_framework import permissions


class JobPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user making the request is the creator of the job
        if view.action in ["retrieve", "update", "partial_update", "destroy", "list"]:
            return obj.created_by == request.user
        else:
            return request.user.is_authenticated
