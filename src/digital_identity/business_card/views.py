from django.shortcuts import render


def business_card(request):
    return render(request, 'business_card/business_card.html')

def business_card_create(request):
    return render(request, 'business_card/business_card_create.html')

def business_card_update(request):
    return render(request, 'business_card/business_card_update.html')