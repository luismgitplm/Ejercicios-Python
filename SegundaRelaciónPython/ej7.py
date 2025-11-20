"""Escribe un programa que recoja una cadena de texto por teclado y una letra a
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar
el número de veces que se repite la letra en el texto"""
texto = input("Escriba un texto:")
letra = input("Escriba una letra a buscar en ese texto:")
contador = 0

for i in range(len(texto)):
    if texto[i].lower() == letra.lower():
        contador += 1

print(f"Las veces que la letra {letra} se ha repetido en el texto {texto} han sido: {contador}")

