"""1. Escribe un programa que recoja un número e indique si se trata de un número
par o impar."""
num = int(input("Indique un número entero: "))

if num == 0:
    print("Es cero.")
elif num%2 == 0:
    print("Es un número par.")
else:
    print("Es un número impar.")