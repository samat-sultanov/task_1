from django.urls import path
from webapp.views import math_numbers


urlpatterns = [
    path('', math_numbers)
]
