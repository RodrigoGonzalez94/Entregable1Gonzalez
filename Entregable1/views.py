from pydoc import render_doc
from re import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def about(request):
    
    template = loader.get_template('about.html')
    
    render = template.render({})
    
    return HttpResponse(render)