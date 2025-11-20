"""Escribe un programa que recoja un número de filas y columnas, y muestre una
tabla con tantas filas y columnas como indicadas, numerando las celdas de
izquierda a derecha y de arriba abajo. Por ejemplo, si se introducen 2 filas y 3
columnas, se debe mostrar:
"""
filas = int(input("Indique el número de filas."))
columnas = int (input("Indique el número de columnas."))
numero = 1

for i in range(filas):
    for j in range(columnas):
        print(numero, end=" ")
        numero += 1
    print("\n")