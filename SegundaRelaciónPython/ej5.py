"""Escribe un programa que recoja un número por teclado y muestre los primeros
cuadrados hasta llegar al número introducido. Por ejemplo, si se ha
introducido el valor 5, se debe mostrar:"""
numero = int(input("Indique un número"))
for i in range(1,numero + 1):
    print(pow(i,2), end=" ")