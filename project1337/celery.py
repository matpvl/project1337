"""Celery configuration."""

import os

from django.conf import settings
from celery.app import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1337.settings")

app = Celery("project1337", broker=settings.CELERY_BROKER_URL)

# Read config from Django settings with the 'CELERY' prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks from installed apps and `tasks.py`.
app.autodiscover_tasks(["project1337.tasks"])
