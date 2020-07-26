from django.urls import path
from .api import send

urlpatterns = [
    path('send', send),
]
