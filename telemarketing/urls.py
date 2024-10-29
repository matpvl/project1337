"""Urls for the telemarketing app."""

from django.urls import path
from telemarketing.views import contact_view, success_view

urlpatterns = [
    path("", contact_view, name="contact"),  # Root path for contact form
    path("success/", success_view, name="success"),  # Path for success message
]
