from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Task
from .serializers import TaskSerializer

class TaskView(CreateAPIView,ListAPIView):
  authentication_classes = [JWTAuthentication]
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
