"""3. Escribe un programa que lea tres números y que muestre los números mayor
y menor."""
num1 = int(input("Indique un número entero:"))
num2 = int(input("Indique un segundo número entero:"))
num3 = int(input("Indique un tercer número entero:"))
max = max(num1,num2,num3)
min = min(num1,num2,num3)

print(f"El valor máximo indicado es {max}. El valor mínimo es {min}")