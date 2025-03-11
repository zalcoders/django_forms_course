from django.db import models


class Interest(models.Model):
    title = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, default="fa-solid fa-check")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    first_name = models.CharField(max_length=254)
    last_name  = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    interests = models.ManyToManyField("newsletter.Interest", blank=True)
    agreed_to_poicies = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
