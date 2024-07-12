from django.urls import path
from .views import send_token

urlpatterns = [
    path('', send_token, name="whatsapp_api"),
]