from django.shortcuts import render
from django.shortcuts import redirect
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
    if request.method == 'GET':
        return render(request, 'crearAutor.html', {'autor_form': AutorForm})
        return (request, 'nombre_carpeta/crearAutor.html')
        
    if request.method == 'POST':
        
        form=AutorForm(data=request.POST)
        
    if form.is_valid: 
        form.save() 
        return redirect ('/author/') 
    else:
        form=AutorForm(data=request.POST)
        return render (request, 'crearAutor.html',{'autor_form': AutorForm}) 
    
def editarAutor (request, pk=None): #Recibe la clave del autor que queremos actualizar.
    autor=Author.objects.get(pk=pk) #Nos buscará el registro que coincida con la clave que le
    author_form=AutorForm(instance=autor) #todo form basado en un modelo tiene este atributo que hace

    if request.method == 'GET':
        author_form=AutorForm(instance=autor) 
        return render (request,'editarAutor.html',{'author':autor,'author_form':author_form}) 
    if request.method == 'POST':
        author_form=AutorForm(data=request.POST, instance=autor) 
    if author_form.is_valid():
        author_form.save()
        return redirect ('/author/') #Se realiza igual que en la creación
    else: 
        author_form=AutorForm(data=request.POST, instance=autor)
        return render (request,'editarAutor.html',{'author':autor,'author_form':author_form})
    

def eliminarAutor (request, pk=None):
    Author.objects.filter(pk=pk).delete()
    #Otra forma de hacerlo
    #autor=Author.objects.get(pk=pk)
    #autor.delete()
    return redirect ('/author/')
    

    
    
