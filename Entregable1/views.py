from pydoc import render_doc
from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def home(request):
    
    template = loader.get_template('index.html')
    
    render = template.render({})
    
    return HttpResponse(render)

def acerca_de(request):
    
    template = loader.get_template('acerca_de.html')
    
    render = template.render({})
    
    return HttpResponse(render)