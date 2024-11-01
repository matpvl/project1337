"""View for the telemarketing app."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from project1337.tasks import contact_person_via_phone
from telemarketing.forms import TargetedContactForm
from telemarketing.models import TargetedContact


def contact_view(request: HttpRequest) -> HttpResponse:
    """View for contact page."""
    form = TargetedContactForm(request.POST or None)
    contacts = TargetedContact.objects.all().order_by("-call_started_at")

    if form.is_valid():
        contact = form.save()
        # trigger celery task.
        contact_person_via_phone.delay(contact.id)
        # Redirect to the same view after form submission to avoid resubmission on refresh
        return redirect("contact")

    return render(request, "telemarketing/contact_form.html", {"form": form, "contacts": contacts})
