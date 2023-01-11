from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    UpdateAPIView,
    ListAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListAndSoftDeleteToken(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        user_obj = get_object_or_404(User, pk=user_id)
        user = User.objects.filter(pk=user_obj.id)
        return user

    def delete(self, request, *args, **kwargs):
        self.request.user.is_active = False
        self.request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
