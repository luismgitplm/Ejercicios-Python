'''2. Definir una función que, al recibir una cadena de texto, cuente cuántas palabras hay y
devuelva dicho valor.'''
import re

def contarPalabras(texto):
    listaPalabras  = re.split(r'\s+',texto)
    return (len(listaPalabras))

print(contarPalabras("Hola, buenas          tardes"))