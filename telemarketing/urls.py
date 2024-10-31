"""Urls for the telemarketing app."""

from django.urls import path
from telemarketing.views import contact_view

urlpatterns = [
    path("", contact_view, name="contact"),  # Root path for contact form
]
