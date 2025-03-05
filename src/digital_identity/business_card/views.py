from django.shortcuts import render
from business_card.forms import SampleForm


def business_card(request):
    return render(request, 'business_card/business_card.html')

def business_card_create(request):
    sample_form = SampleForm()
    submitted = False
    if request.method == "POST":
        sample_form = SampleForm(request.POST)
        if sample_form.is_valid():
            print(sample_form.cleaned_data)
            print(dir(sample_form.fields["email"]))
            print(sample_form.fields["email"].required)
            submitted = True

    return render(request, 'business_card/business_card_create.html', {"sample_form": sample_form, "submitted": submitted})

def business_card_update(request):
    return render(request, 'business_card/business_card_update.html')