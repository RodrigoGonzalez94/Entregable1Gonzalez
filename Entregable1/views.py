from pydoc import render_doc
from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import Usuarios
from .forms import FormUsuarios, BusquedaUsuario
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    Función nos llevará al template index.html 
    
    """
    return render(request, 'index.html')

def formulario(request):
    """
    Función que toma la información que el usuario le proporcione
    la guardará, y redirigirá al listado de todos los uduarios que se han guradado.
    
    """
    if request.method == 'POST':
        form = FormUsuarios(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            usuario = Usuarios(
                nombre = data.get('nombre'),
                edad = data.get('edad'),
                fecha_nacimiento = data.get('fecha_nacimiento'),
                ocupacion = data.get('ocupacion')
            )
            usuario.save()
            return redirect('listado_usuarios')
        
        else:
            return render(request, 'formulario_usuarios.html', {'form': form})
            
    
    form_usuario = FormUsuarios()
    

    return render(request, 'formulario_usuarios.html', {'form': form_usuario})

def listado_usuarios(request):
    """
    Hace una busqueda por la clase 'nombre', devuelve todos las coincidencias.
    
    """   
    nombre_de_busqueda = request.GET.get('nombre')
    
    if nombre_de_busqueda:
        listado_usuarios = Usuarios.objects.filter(nombre__icontains=nombre_de_busqueda) 
    else:
        listado_usuarios = Usuarios.objects.all()
    
    form = BusquedaUsuario()
    return render(request, 'usuarios.html', {'listado_usuarios': listado_usuarios, 'form': form})


def about(request):
    """
    Función nos llevará al template about.html 
    
    """
    
    template = loader.get_template('about.html')
    
    render = template.render({})
    
    return HttpResponse(render)

@login_required
def editar_usuario(request, id):
    """
    Función para poder editar la información ya ingresada en el formulario.
    
    """   
    usuario = Usuarios.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormUsuarios(request.POST)
        if form.is_valid():
            usuario.nombre = form.cleaned_data.get('nombre')
            usuario.edad = form.cleaned_data.get('edad')
            usuario.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            usuario.ocupacion = form.cleaned_data.get('ocupacion')
            usuario.save()
    
            return redirect('listado_usuarios')
        
        else:
            return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})
            
    form_usuario = FormUsuarios(initial={'nombre': usuario.nombre, 'edad': usuario.edad, 'fecha_nacimiento': usuario.fecha_nacimiento, 'ocupacion': usuario.ocupacion})
    
    return render(request, 'editar_usuario.html', {'form': form_usuario, 'usuario': usuario})

@login_required
def eliminar_usuario(request, id):
    """
    Función para poder eliminar la información ya ingresada en el formulario.
    
    """ 
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    return redirect('listado_usuarios')

def mostrar_usuario(request, id):
    """
    Función para visualizar la información ya ingresada en el formulario.
    
    """ 
    usuario = Usuarios.objects.get(id=id)
    return render(request, 'mostrar_usuario.html', {'usuario': usuario})