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
        phone_number = str(self.cleaned_data.get("phone_number"))
        self._is_valid_phone_number(phone_number)
        if TargetedContact.objects.filter(phone_number=phone_number).exists():
            error_data = "This phone number is already in use."
            raise forms.ValidationError(error_data)
        return phone_number

    @staticmethod
    def _is_valid_phone_number(phone_number: str) -> None:
        """Check whether this is a phone number."""

        # current check is only for digits and len in order to not complicate
        # a larger application would need deeper checks and probably a library or two

        if not int(phone_number):
            error_data = "Phone number must consist of only digits."
            raise forms.ValidationError(error_data)
        if len(phone_number) >= 15:
            error_data = "Phone number must not exceed 15 digits."
            raise forms.ValidationError(error_data)

