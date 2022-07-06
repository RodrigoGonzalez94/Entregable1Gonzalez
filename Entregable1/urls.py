from django.urls import path
from .views import home, about, listado_usuarios, formulario


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name= 'about'),
    path("usuarios/", listado_usuarios, name='listado_usuarios'),
    path('formulario/', formulario, name= 'formulario'),
]