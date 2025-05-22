from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User

class IsAdminUserType(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == User.UserType.ADMIN

    def has_object_permission(self, request, view, obj):
        return request.user.user_type == User.UserType.ADMIN

class IsAdminOrReadOnly(IsAdminUserType):
    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            or request.method in SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return (
            super().has_object_permission(request, view, obj)
            or request.method in SAFE_METHODS
        )
