from django.shortcuts import render
from newsletter.forms import SubscriptionModelForm
from newsletter.models import Subscription


def index(request):
    submitted = False
    if request.method == "POST":
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = SubscriptionModelForm()
    return render(request, "newsletter/index.html", {"form": form, "submitted": submitted})


def test_view(request):
    if request.method == "POST":
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubscriptionModelForm()

    return render(request, "newsletter/test.html", {"form": form})


def test_update_view(request, pk):
    instance = Subscription.objects.get(pk=pk)
    if request.method == "POST":
        form = SubscriptionModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = SubscriptionModelForm(instance=instance)

    return render(request, "newsletter/test.html", {"form": form})

