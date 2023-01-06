from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response

from .models import Invite


class InviteView(APIView):
    def get(self, request: Request, invite_id: int) -> Response:
        invite = get_object_or_404(Invite, id=invite_id)
        invite.is_accept = True
        invite.save()
        return HttpResponse("Compromisso aceito com sucesso")
