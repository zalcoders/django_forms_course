from django.shortcuts import render
from business_card.forms import BusinessCardForm
from business_card.models import BusinessCard


def business_card(request, slug):
    business_card = BusinessCard.objects.get(slug=slug)
    return render(request, 'business_card/business_card.html', {"business_card": business_card})

def business_card_create(request):
    business_card = BusinessCardForm()
    success = False
    obj = None
    errors = []
    if request.method == "POST":
        business_card = BusinessCardForm(request.POST, request.FILES)
        if business_card.is_valid():
            obj = BusinessCard(**business_card.cleaned_data)
            obj.save()
            success = True
        else:
            errors = business_card.errors


    return render(request, 'business_card/business_card_create.html', {"business_card": business_card, "success": success, "errors": errors, "obj": obj})

def business_card_update(request):
    return render(request, 'business_card/business_card_update.html')