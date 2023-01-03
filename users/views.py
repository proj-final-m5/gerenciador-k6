from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from .serializers import UserSerializer
from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()

