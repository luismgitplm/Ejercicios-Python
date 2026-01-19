from django.shortcuts import render
from HolaMundo.models import Author
from HolaMundo.models import Book
from django.http import HttpResponse
from HolaMundo.forms import AutorForm


# Create your views here.

def hola_mundo (request): # El request captura las peticiones de los clientes
    return HttpResponse ("<h1>hola mundo</h1>")

def home (request): # Pinta una página con render, también hay que darlo de alta en urls.py
    return render(request,'index.html')# Aquí se manda la variable authors (objects.all()) a la página index.html (en home)

def author (request):
    author = Author.objects.all()
    return render(request,'author.html',{'authors': author})

def book (request):
    book = Book.objects.all()
    return render(request, 'book.html',{'books': book})

def crearAutor (request):
    return render(request, 'crearAutor.html',{'autor_form': AutorForm})
    
