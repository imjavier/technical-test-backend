from rest_framework.permissions import BasePermission
from users.models import User

class IsAdminUserType(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == User.UserType.ADMIN

    def has_object_permission(self, request, view, obj):
        return request.user.user_type == User.UserType.ADMIN
