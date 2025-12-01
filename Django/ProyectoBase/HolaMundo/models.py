from django.db import models

# Create your models here.
class Author (models.Model):
    name=models.CharField (verbose_name='Nombre', # etiqueta dentro de la tabla
    max_length= 100,
    default=''
    )
    last_name=models.CharField(verbose_name='Apellido',
    max_length=150,
    default='')
    age=models.PositiveSmallIntegerField (verbose_name='Edad',)
    mail=models.EmailField(verbose_name='email',max_length=150,default='')
    

    def __str__(self):
        return f'{self.name} {self.last_name}'