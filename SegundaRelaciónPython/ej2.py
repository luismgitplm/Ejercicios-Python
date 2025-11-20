"""2. Escribe un programa que recoja un número y calcule su factorial."""
num = int(input("Escriba un número entero positivo:"))

factorial = 1
for i in range(1,num + 1):
    factorial *= i

print("El factorial de ese número es: ",factorial)