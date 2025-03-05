from django import forms 

class SampleForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50, required=False)
    last_name = forms.CharField(label="Last Name", max_length=50, required=False)
    email = forms.EmailField(label="Email", required=True, help_text="What is your email address?")
