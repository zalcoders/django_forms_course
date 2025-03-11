from django import forms
from newsletter.models import Subscription


class SubscriptionModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.template_name = "forms/text_input.html"
        self.fields['last_name'].widget.template_name = "forms/text_input.html"
        self.fields['email'].widget.template_name = "forms/email_input.html"
        self.fields['agreed_to_poicies'].widget.template_name = "forms/boolean_input.html"
        self.fields['interests'].widget.template_name = "forms/interests_input.html"

    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'email', 'interests', 'agreed_to_poicies']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Your last name",
                'custom_label': "First Name"
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Your first name",
                'custom_label': "Last Name"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "your.email@example.com",
                'custom_label': "Email Address"
            }),
            'agreed_to_poicies': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'custom_label': "I agree to the Privacy Policy and consent to receive emails."
            }),
            'interests': forms.CheckboxSelectMultiple()
        }
