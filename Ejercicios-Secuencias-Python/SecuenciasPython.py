import cmath
def secuencia_numeros():
    flag = False 
    numeros = []
    

    while not flag:
        num = int(input("Indique un número entero: "))
        while (cmath.isnan(num)):
            num = int(input("Lo indicado no era un número, inténtelo de nuevo:"))
        if num == 0:
            flag = True
        else:
            numeros.append(num)

    print("Los números en el orden en el que se indicaron:\n")
    for num in numeros:
        print(num,end=" ")

    print("\nLos números en orden creciente")
    numeros.sort()
    for num in numeros:
        print(num,end=" ")
    
    print("\nLos números en orden decreciente")
    numeros.sort(reverse = True)
    for num in numeros:
        print(num,end=" ")

def secuencia_textos():
    flag = False
    textos = []

    while not flag:
        texto = input("Escriba un texto, excriba una cadena vacía para finalizar")

        if texto.isspace() or texto == '':
            flag = True
        else:
            textos.append(texto)

    # Esta vez empleando el método sorted(). Útil en caso de que se quiera conservar la lista original
    textosCreciente = sorted(textos)
    textosDecreciente = sorted(textos,reverse=True)

    print("Los textos en el orden indicado:")
    for t in textos:
        print(t)
    
    print("Los textos en orden alfabético:")
    for t in textosCreciente:
        print(t)
    
    print("Los textos en orden alfabético descendiente:")
    for t in textosDecreciente:
        print(t)


def palindromo(s) -> bool:
    esPalindromo = False
    if s.lower() == s.lower()[::-1]:
        esPalindromo = True

    return esPalindromo

def palindromo2(s1,s2):
    opcion = input("Escribe a si quieres distinguir entre mayúsculas y b si no")
    if opcion.lower() == "a":
        if s1 == s2[::-1]:
            print("Las cadenas son palíndromos respectivos case sensitive")
        else:
            print("Las cadenas no son palíndromos respectivos case sensitive")
    else:
        if s1.lower() == s2.lower()[::-1]:
            print("Las cadenas son palíndromos respectivos case insensitive")
        else:
            print("Las cadenas no son palíndromos respectivos case insensitive")
            
flag = False

while not flag:
    opcion = input("Indica una opción: a,b,c,d. Indique cualquier otro caracter para salir: ")

    if opcion.lower() == "a":
        secuencia_numeros()
    elif opcion.lower() == "b":
        s = input("Indique una cadena para ver si es palíndromo")
        palindromo()
    elif opcion.lower() == "c":
        print("Indique dos cadenas de caracteres para ver si son palíndromos respectivos")
        s1 = input()
        s2 = input()
        palindromo2(s1,s2)
    elif opcion.lower() == "d":
        secuencia_textos()
    else:
        print("Fin del programa")
        flag = True



