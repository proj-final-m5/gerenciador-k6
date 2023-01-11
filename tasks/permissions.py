from rest_framework import permissions
from rest_framework.views import Request, View

from invites.models import Invite

from .models import Task


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Task) -> bool:
        if request.user.id == obj.user_id:
            return True

        invites = list(Invite.objects.filter(task_id=obj.id))
        for invite in invites:
            if (request.user.email == invite.contact.email and invite.is_admin) or (
                request.user.email == invite.contact.email and request.method == "GET"
            ):
                return True

        return False
