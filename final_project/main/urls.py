from django.urls import path
from .views import indexurlpatterns = [
    path('', index, name="index")
]
