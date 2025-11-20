'''1. Definir una función que, al recibir una cadena de texto, cuente cuántas vocales hay y
devuelva dicho valor.'''
import re

def contarVocales(texto):
    contador = 0
    for caracter in texto:
        if re.match(r'[aeiouáéíóúäëïöü]',caracter.lower()):
            contador += 1
    return contador

print(contarVocales("HOLA, qué tal"))