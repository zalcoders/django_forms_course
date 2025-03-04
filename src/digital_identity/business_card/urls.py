from django.urls import path
from business_card.views import business_card, business_card_create, business_card_update

app_name = 'business_card'
urlpatterns = [
    path('', business_card, name='business_card'),
    path('create/', business_card_create, name='business_card_create'),
    path('update/', business_card_update, name='business_card_update'),
]
