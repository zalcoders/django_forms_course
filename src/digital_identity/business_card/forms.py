from django import forms
from django.core.exceptions import ValidationError
import re


def normalize_persian_digits(mobile):
    data = {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9",
    }

    for fa, en in data.items():
        mobile = mobile.replace(fa, en)
    return mobile


def validate_and_normalize_irani_mobile_phone(mobile):
    if not mobile:
        return mobile

    mobile = normalize_persian_digits(mobile)

    digits_only = re.sub(r'\D', '', mobile)

    if digits_only.startswith("0"):
        digits_only = digits_only[1:]
    elif digits_only.startswith("98"):
        digits_only = digits_only[2:]

    if len(digits_only) != 10 or not digits_only.startswith("9"):
        raise ValidationError(f"Invalid Mobile Number: {mobile}")

    return f"98{digits_only}"

class SampleForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50, required=False)
    last_name = forms.CharField(label="Last Name", max_length=50, required=False)
    email = forms.EmailField(label="Email", required=True, help_text="What is your email address?")


class BusinessCardForm(forms.Form):
    profile_picture = forms.ImageField()
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    job_title = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(max_length=100, required=False)
    landline_number = forms.CharField(max_length=100, required=False)
    business_name = forms.CharField(max_length=100, required=False)
    website = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=100, required=False)
    description = forms.TextInput()
    linkedin_profile = forms.CharField(max_length=100, required=False)
    x_profile = forms.CharField(max_length=100, required=False)
    instagram_profile = forms.CharField(max_length=100, required=False)
    needs_qr = forms.BooleanField(required=False)
    username = forms.CharField(max_length=100, required=False)
    password = forms.CharField(max_length=100, required=False)
    marcketing_check = forms.BooleanField(required=False)

    def clean_phone_number(self):
        mobile = self.cleaned_data["phone_number"]
        if mobile:
            mobile = validate_and_normalize_irani_mobile_phone(mobile)
        return mobile
    
    def clean(self):
        cleaned_data = super().clean()
        landline_number = cleaned_data.get("landline_number", None)
        phone_number = cleaned_data.get("phone_number", None)

        if not phone_number and not landline_number:
            raise ValidationError("You must eigther set phone number or landline number")
