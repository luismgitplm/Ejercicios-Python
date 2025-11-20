"""Escribe un programa que recoja un número impar. Debe asegurarse de que
sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez
tenga el número impar debe mostrar una pirámide de asteriscos cuya base es
igual al número introducido. Por ejemplo, si se introduce el valor 7 se debe
mostrar:"""
numero = int(input("Escriba un número entero impar."))
while numero % 2 == 0:
    numero = int(input("El número indicado era par, escriba uno impar."))

numAst = 1

for i in range(numero,0,-2):
    print(" "*(i // 2),"*"*numAst)
    numAst += 2

"""for i in range(numero // 2 + 1):
    print(" "*((numero // 2) - i),"*"*(2*i + 1))"""




