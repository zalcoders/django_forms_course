from django import forms
from newsletter.models import Subscription


class SubscriptionModelForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'email', 'interests', 'agreed_to_poicies']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter your name"
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter your name"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter your name"
            }),
            'agreed_to_poicies': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'interests': forms.CheckboxSelectMultiple()
        }
