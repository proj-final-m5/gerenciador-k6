from django.urls import path
from . import views

urlpatterns = [path("user/invite/<int:invite_id>/", views.InviteView.as_view()),]
