from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

class TaskView(CreateAPIView,ListAPIView):
  authentication_classes = [JWTAuthentication]
  queryset = Task.objects.all()
  serializer_class = TaskSerializer
  def perform_create(self, serializer):
        categories = get_object_or_404(Task, self.request.body.categories)
        serializer.save(user=self.request.user,categories=categories)

class TaskDetailView(RetrieveUpdateDestroyAPIView):
  authentication_classes = [JWTAuthentication]
  queryset= Task.objects.all()
  serializer_class = TaskSerializer