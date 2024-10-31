"""Django models."""

from django.db import models


class TargetedContact(models.Model):
    """Targeted contact person for the telemarketing campaign."""

    phone_number = models.CharField(max_length=15, unique=True)
    reply = models.CharField(max_length=255, blank=True, default=None)
    status = models.CharField(max_length=20, default="PENDING")

    def __str__(self) -> str:
        """Return string representation of Targeted Contact."""
        return f"{self.phone_number} - {self.status} - {self.reply}"
