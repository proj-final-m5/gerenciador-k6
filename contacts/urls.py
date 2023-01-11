from django.urls import path
from . import views

urlpatterns = [
    path("user/contact/", views.ContactCreateView.as_view()),
    path("user/contacts/", views.ContactListView.as_view()),
    path("user/contact/<int:pk>/", views.ContactDetailView.as_view()),
]
