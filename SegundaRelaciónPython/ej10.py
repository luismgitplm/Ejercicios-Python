"""Escribe un programa que recoja un número y muestre un triángulo formado
por secuencias decrecientes de números impares."""
numero = int(input("Indique un número entero "))
a = 1

for _ in range(numero):
    for i in range(a,0,-2):
        print(i,end=" ")
    print("")
    a += 2 

