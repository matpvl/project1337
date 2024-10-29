"""File containing Celery tasks."""

from celery import shared_task

@shared_task
def add(x, y):
    """Simple celery addition task."""
    return x + y
