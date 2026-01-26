from django import forms
from HolaMundo.models import Author # importamos el modelo que nos hace falta, en este caso
from HolaMundo.models import Book
#Creamos nuestro primer Form
class AutorForm (forms.ModelForm): #Vamos a crear un formulario de Django , basado en un
    #Los forms de django tienen su clase meta, dónde indicamos el modelo al cual hacemos
    #Con estas dos clases lo que estamos diciendo es que Django debe crearnos un form que haga
    class Meta:
        model=Author
        fields='__all__'

class BookForm (forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'