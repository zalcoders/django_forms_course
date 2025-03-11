from django.urls import path
from newsletter.views import index, test_view, test_update_view

app_name = "newsletter"
urlpatterns = [
    path('', index, name="home"),
    path('test/', test_view, name="test"),
    path('test_update/<int:pk>', test_update_view, name="test_update"),
]
