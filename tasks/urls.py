from django.urls import path
from . import views


urlpatterns = [
    path("user/tasks/", views.TaskView.as_view()),
    path("user/tasks/<int:pk>/", views.TaskDetailView.as_view()),
]
