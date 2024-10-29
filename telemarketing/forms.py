"""Forms for the telemarketing app."""

from django import forms

from telemarketing.models import TargetedContact


class TargetedContactForm(forms.ModelForm):
    """Form holding the input for a contacts phone number."""

    class Meta:
        """Meta class."""

        model = TargetedContact
        fields = ["phone_number"]
