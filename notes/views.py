from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import NoteSerializer, Note
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsPermission, IsUser


# Create your views here.
class NoteView(CreateAPIView, ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPermission]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user_id=user.id)


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUser]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
