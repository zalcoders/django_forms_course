from django.urls import path
from newsletter.views import index

app_name = "newsletter"
urlpatterns = [
    path('', index, name="home"),
]
