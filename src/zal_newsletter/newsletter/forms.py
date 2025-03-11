from django import forms
from newsletter.models import Subscription


class SubscriptionModelForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'email', 'interests', 'agreed_to_poicies']
