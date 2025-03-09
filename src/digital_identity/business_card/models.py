from django.db import models
from uuid import uuid4


class BusinessCard(models.Model):
    slug = models.SlugField(max_length=50, default=uuid4, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    landline_number = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    website = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    description = models.TextField()
    category = models.CharField(max_length=512)
    linkedin_profile = models.CharField(max_length=254)
    x_profile = models.CharField(max_length=254)
    instagram_profile = models.CharField(max_length=254)
    needs_qr = models.BooleanField()
    username = models.CharField(max_length=50, unique=True, default=uuid4)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    marcketing_check = models.BooleanField()
