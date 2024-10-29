"""File containing Celery tasks."""

import time
from celery import shared_task

from telemarketing.models import TargetedContact
from telemarketing.quote_generation import miss_the_old_kanye


@shared_task
def add(x, y):
    """Simple celery addition task."""
    return x + y


@shared_task
def contact_person_via_phone(contact_id):
    """Simulate a phone call that takes 120 seconds and update DB status."""
    time.sleep(120)  # Simulate long-running task
    contact = TargetedContact.objects.get(id=contact_id)
    contact.reply = miss_the_old_kanye()
    contact.status = "DONE"
    contact.save()
