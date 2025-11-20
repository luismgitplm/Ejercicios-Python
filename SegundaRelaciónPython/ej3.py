"""3. Escribe un programa que recoja números por teclado hasta que se introduzca
el valor cero. A continuación, debe mostrar el número de valores introducidos,
el valor mínimo introducido, el máximo, la suma de todos ellos y su media
aritmética (todos los cálculos sin contar el cero)"""
numero = int(input("Indique números enteros. Escriba cero para finalizar."))

if numero == 0:
    print("Fin del programa.")
else:
    contador = 1
    minimo = numero
    maximo = numero
    media = numero
    suma = numero

    while numero != 0:
        numero = int(input())
        if numero != 0:
            contador += 1
            minimo = min(minimo,numero)
            maximo = max(maximo,numero)
            suma += numero
    
    media = suma / contador

    print(f"Fin del programa \n El número de valores introducidos ha sido: {contador} / El valor máximo introducido ha sido: {maximo} / El valor mínimo introducido ha sido: {minimo} / La media de los valores es: {media} / La suma de los valores es: {suma}")
