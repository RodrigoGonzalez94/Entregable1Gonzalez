from django.urls import path
from .views import home, about, listado_usuarios, formulario, editar_usuario, eliminar_usuario, mostrar_usuario


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name= 'about'),
    path("usuarios/", listado_usuarios, name='listado_usuarios'),
    path('formulario/', formulario, name= 'formulario'),
    path('editar-usuario/<int:id>/', editar_usuario, name='editar_usuario'),
    path('eliminar-usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('mostrar-usuario<int:id>/', mostrar_usuario, name='mostrar_usuario'),   
]