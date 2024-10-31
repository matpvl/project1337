"""File containing Celery tasks."""

import time
from celery import shared_task
from django.utils import timezone

from telemarketing.models import TargetedContact
from telemarketing.quote_generation import miss_the_old_kanye


@shared_task
def add(x, y):
    """Simple celery addition task."""
    return x + y


@shared_task
def contact_person_via_phone(contact_id):
    """Simulate a phone call that takes 120 seconds and update DB status."""
    contact = TargetedContact.objects.get(id=contact_id)
    contact.call_started_at = timezone.now()
    contact.save(update_fields=["call_started_at"])

    # Simulate a 2 minute phone call
    time.sleep(120)

    contact.reply = miss_the_old_kanye()
    contact.status = "DONE"
    contact.call_ended_at = timezone.now()
    contact.save(update_fields=["reply", "status", "call_ended_at"])
