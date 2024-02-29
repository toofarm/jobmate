from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user making the request is the creator of the job
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user
