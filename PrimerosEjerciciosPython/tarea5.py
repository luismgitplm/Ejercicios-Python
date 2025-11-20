"""5. Escribe un programa que recoja un número y muestre su valor absoluto."""
num = int(input("Indique un número: "))
if num<0:
    absoluto = num*(-1)
else:
    absoluto = num

print("El valor absoluto del número indicado es: ",absoluto)