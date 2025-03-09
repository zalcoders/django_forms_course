from django.shortcuts import render
from business_card.forms import BusinessCardForm
from business_card.models import BusinessCard

from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password, make_password


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
        username = business_card.data["username"]
        try:
            BusinessCard.objects.get(username=username)
            errors.append(f"Username {username} already taken")
        except BusinessCard.DoesNotExist:
            pass
        except Exception as e:
            raise

        categories_text = business_card.data["category"]
        if categories_text.endswith(","):
            categories_text = categories_text[:-1]
        if categories_text:
            categories = categories_text.split(",")
        if business_card.is_valid():
            data = business_card.cleaned_data
            data["password"] = make_password(business_card.cleaned_data["password"])
            obj = BusinessCard(**data)
            obj.save()
            success = True
        else:
            errors = business_card.errors


    return render(request, 'business_card/business_card_create.html', {"business_card": business_card, "categories": categories, "success": success, "errors": errors, "obj": obj})

def business_card_update(request, slug):
    success = False
    obj = BusinessCard.objects.get(slug=slug)
    errors = []
    if request.method == "POST":
        print(request.FILES)
        business_card = BusinessCardForm(request.POST, request.FILES)
        if business_card.is_valid():
            print(business_card.cleaned_data["password"])
            print(check_password(business_card.cleaned_data["password"], obj.password))
            if obj.username != business_card.cleaned_data["username"]:
                business_card.add_error(None, "Username or Password is wrong....")
            elif not check_password(business_card.cleaned_data["password"], obj.password):
                business_card.add_error(None, "Username or Password is wrong....")
            else:
                data = business_card.cleaned_data
                del data["password"]
                del data["profile_picture"]
                obj.profile_picture = request.FILES.get("profile_picture")
                obj.save()
                BusinessCard.objects.filter(slug=slug).update(**data)
                success = True
    else:
        data = model_to_dict(obj)
        del data['id']
        del data['profile_picture']
        del data['slug']
        del data['username']
        del data['password']
        business_card = BusinessCardForm(initial=data)
        

    categories = []
    categories_text = obj.category
    if categories_text.endswith(","):
        categories_text = categories_text[:-1]
    if categories_text:
        categories = categories_text.split(",")

    errors = business_card.errors
    return render(request, 'business_card/business_card_update.html', {"business_card": business_card, "categories": categories, "success": success, "errors": errors, "obj": obj})