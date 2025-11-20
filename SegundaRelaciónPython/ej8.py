"""Escribe un programa que recoja un número y calcule si es primo."""
numero = int(input("Indique un número "))
esPrimo = True
divisor = 2

while esPrimo and divisor < numero:
    if numero % divisor == 0:
         esPrimo = False 
    divisor += 1


if esPrimo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")