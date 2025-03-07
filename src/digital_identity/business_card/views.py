from django.shortcuts import render
from business_card.forms import BusinessCardForm
from business_card.models import BusinessCard


def business_card(request):
    return render(request, 'business_card/business_card.html')

def business_card_create(request):
    business_card = BusinessCardForm()
    success = False
    errors = []
    if request.method == "POST":
        business_card = BusinessCardForm(request.POST, request.FILES)
        if business_card.is_valid():
            BusinessCard(**business_card.cleaned_data).save()
            success = True
        else:
            errors = business_card.errors

    return render(request, 'business_card/business_card_create.html', {"business_card": business_card, "success": success, "errors": errors})

def business_card_update(request):
    return render(request, 'business_card/business_card_update.html')