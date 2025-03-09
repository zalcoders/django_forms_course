from django.shortcuts import render
from business_card.forms import BusinessCardForm
from business_card.models import BusinessCard


def business_card(request, slug):
    business_card = BusinessCard.objects.get(slug=slug)
    categories = business_card.category.split(",")
    return render(request, 'business_card/business_card.html', {"business_card": business_card, "categories": categories})

def business_card_create(request):
    business_card = BusinessCardForm()
    success = False
    obj = None
    errors = []
    categories = []
    if request.method == "POST":
        business_card = BusinessCardForm(request.POST, request.FILES)
        categories_text = business_card.data["category"]
        if categories_text.endswith(","):
            categories_text = categories_text[:-1]
        if categories_text:
            categories = categories_text.split(",")
        if business_card.is_valid():
            obj = BusinessCard(**business_card.cleaned_data)
            obj.save()
            success = True
        else:
            errors = business_card.errors


    return render(request, 'business_card/business_card_create.html', {"business_card": business_card, "categories": categories, "success": success, "errors": errors, "obj": obj})

def business_card_update(request):
    return render(request, 'business_card/business_card_update.html')