from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_superuser
        )


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: User):
        return (
            obj.email == request.user.email
            or request.user.is_superuser
        )
