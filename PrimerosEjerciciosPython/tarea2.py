""" 2. Escribe un programa que recoja dos números enteros por teclado y muestre
los siguientes resultados: suma, resta, multiplicación, división real, división
entera, resto de la división entera y potencia. """

num1 = int(input("Indique un número entero: "))
num2 = int (input("Indique otro número entero: "))
suma = num1+num2
resta = num1-num2
producto = num1*num2
division = num1/num2
divEntera = num1//num2
resto = num1%num2
potencia = num1**num2

print("La suma de ambos números es: {}\n" \
"La diferencia de ambos números es: {}\n" \
"El producto de ambos números es: {}\n" \
"La división real de ambos números es: {}\n" \
"La división entera es: {}\n" \
"El resto de la división es: {}\n" \
"La potencia del primer número elevado al segundo es: {}".format(suma,resta,producto,division,divEntera,resto,potencia))
