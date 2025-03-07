from django.shortcuts import render
from business_card.forms import BusinessCardForm
from business_card.models import BusinessCard


def business_card(request):
    return render(request, 'business_card/business_card.html')

def business_card_create(request):
    business_card = BusinessCardForm()
    submitted = False
    if request.method == "POST":
        business_card = BusinessCardForm(request.POST, request.FILES)
        if business_card.is_valid():
            print(business_card.cleaned_data)
            BusinessCard(**business_card.cleaned_data).save()
            submitted = True
        else:
            print(business_card.errors)

    return render(request, 'business_card/business_card_create.html', {"business_card": business_card, "submitted": submitted})

def business_card_update(request):
    return render(request, 'business_card/business_card_update.html')