from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from contacts.permissions import IsAccountOwner

from .models import Task
from .serializers import TaskSerializer


class TaskView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = TaskSerializer

    def post(self, request: Request) -> Response:
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user_id=user.id)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
