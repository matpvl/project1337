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
        """Check whether the phone number already exists and validate format."""
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number is None:
            raise forms.ValidationError("Phone number is required.")
        phone_number = str(phone_number).strip()  # Convert to string and strip whitespace
        self._is_valid_phone_number(phone_number)

        if TargetedContact.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already in use.")

        return phone_number

    @staticmethod
    def _is_valid_phone_number(phone_number: str) -> None:
        """Check whether the phone number is valid."""
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must consist of only digits.")
        if len(phone_number) > 15:
            raise forms.ValidationError("Phone number must not exceed 15 digits.")


