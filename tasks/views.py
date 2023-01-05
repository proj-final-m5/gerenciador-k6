from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Task
from .serializers import TaskSerializer

from contacts.permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated

import ipdb


class TaskView(CreateAPIView, ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        ipdb.set_trace()
        print()
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user_id=user.id)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
