from django.urls import path
from Pagina_inicio.views import portada, inicio, subir_comentarios, prueba

urlpatterns = [
    path("Portada/", portada),
    path("", inicio),   
    path("subir-comentarios/",subir_comentarios),
    path('prueba/', prueba, name='probando'),  
    ]
