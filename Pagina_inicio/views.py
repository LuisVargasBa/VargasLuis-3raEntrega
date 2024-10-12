from django.shortcuts import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def portada(request):
    return HttpResponse("Hola")

def inicio(request):
    return HttpResponse("<hi>pagina inicio</h1>")

def subir_comentarios(request):
    return HttpResponse("<hi> Preparando </h1>")

def prueba(request):
    with open(r'templates\prueba.html') as archivo_del_template:
        template = Template(archivo_del_template.read())
    
    contexto = Context()
    
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)
