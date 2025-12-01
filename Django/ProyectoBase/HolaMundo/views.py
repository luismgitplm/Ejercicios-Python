from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def hola_mundo (request): # El request captura las peticiones de los clientes
    return HttpResponse ("<h1>hola mundo</h1>")

def home (request): # Pinta una página con render, también hay que darlo de alta en urls.py
    return render(request,'index.html') # la página index.html hay que crearla dentro del
    
