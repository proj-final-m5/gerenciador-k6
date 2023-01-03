from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from users.serializers import UserSerializer
from .permissions import IsAccountOwner

class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
