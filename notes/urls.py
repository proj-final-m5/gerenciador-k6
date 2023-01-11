from django.urls import path
from .views import NoteView, NoteDetailView

urlpatterns = [
    path("user/note/", NoteView.as_view()),
    path("user/notes/", NoteView.as_view()),
    path("user/note/<int:pk>/", NoteDetailView.as_view()),
]
