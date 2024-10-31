"""Forms for the telemarketing app."""
from typing import Optional

from django import forms

from telemarketing.models import TargetedContact


class TargetedContactForm(forms.ModelForm):
    """Form holding the input for a contacts phone number."""

    class Meta:
        """Meta class."""

        model = TargetedContact
        fields = ["phone_number"]

    def clean_phone_number(self) -> Optional[str]:
        """Check whether the phone number already exists."""
        phone_number = self.cleaned_data.get("phone_number")
        if TargetedContact.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already in use.")
        return phone_number
