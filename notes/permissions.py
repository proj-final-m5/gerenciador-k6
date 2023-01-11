from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated:
            return True

        return False


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        if request.user.is_authenticated and request.user.id == obj.user_id:
            return True

        return False
