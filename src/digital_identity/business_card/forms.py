from django import forms 

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
