from django.urls import path
from .views import home, acerca_de


urlpatterns = [
    path('', home),
    path('acerca-de/', acerca_de),
]