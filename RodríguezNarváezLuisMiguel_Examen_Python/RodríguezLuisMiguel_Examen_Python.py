import re

def pedirEntero(mensaje):
    while True:
        try:
            Valor = int(input(mensaje))
            break
        except ValueError:
            print("No ha indicado un número entero, inténtelo de nuevo: ")
    return Valor

def pedirNumero(mensaje):
    while True:
        try:
            Valor = float(input(mensaje))
            break
        except ValueError:
            print("No ha indicado un número, inténtelo de nuevo: ")
    return Valor


def sustituirVocales():
    texto = input("Indique un frase: ")
    copia = []
    for i in range(len(texto)):
        "Expresión regular que controla tildes y diéresis"
        if re.match(r'[aeiouáéíóúäëïöü]',texto[i].lower()): 
            copia.append('*')
        else:
            copia.append(texto[i])

    print("La frase indicada con las vocales cambiadas por asteriscos: ")
    for i in copia:
        print(i,end='')

'Ejercicio matriz de números impares resuelto'
def numImpares():
    filas = 10
    columnas = 8
    numero = 100

    for i in range(filas):
        'Para hacerlo de este modo se tiene que multiplicar por dos'
        'el número de columnas porque sólo la mitad de las veces se'
        'va a cumplir la condición del if, por lo tanto, el salto de'
        'línea sucedía tras la mitad de los prints esperados'
        for j in range(columnas * 2): 
            if numero % 2 != 0:
                print(numero, end=" ")
            numero -= 1
        print("\n")
    


def pedirNumeros():
    while True:
        cantidadNumeros = pedirEntero("Indique la cantidad de números a introducir:")
        if cantidadNumeros >= 0:
            break
        else:
            print("La cantidad no puede ser un número negativo, inténtelo de nuevo:")
        

    if cantidadNumeros != 0:
        numero = pedirNumero("Indique un número")
        for _ in range(cantidadNumeros - 1):
            numAnterior = numero
            numero = pedirNumero("Indique un número:")
            if numero < numAnterior:
                print("El número indicado ha sido menor que el anterior")
    print("Fin de la sucesión de números.")



def palabraMasLarga():
    texto = input("Indique una frase")
    "Expresión regular que indica que la cadena de caracteres se ha de dividir por espacios"
    listaPalabras = re.split(r'\s+',texto)
    longitudMax = 0
    palabraMasLarga = None

    for i in listaPalabras:
        longitudMax = max(len(i),longitudMax)
        if len(i) == longitudMax:
            palabraMasLarga = i

    print("La palabra más larga de la frase indicada es: " + palabraMasLarga)



def contarCaracteres():
    texto = input("Indique una palabra:")
    aparicionesDeCaracteres = {}

    for i in texto.strip():
        if i.lower() not in aparicionesDeCaracteres:
            aparicionesDeCaracteres[i.lower()] = 1
        else: 
            aparicionesDeCaracteres[i.lower()] += 1
    print("Las apariciones de los distintos caracteres:")
    for i in aparicionesDeCaracteres.items():
        print(i)



flag = False
while not flag:
    print("Escoja una opción:\n"\
    "a) Sustituir vocales\n" \
    "b) Pedir números\n" \
    "c) Recibir la palabra más larga\n" \
    "e) Contar apariciones de caracteres\n" \
    "f) Salir")
    print("")


    opcion = input("Indique una opción: a,b,c,e. escriba f para salir:")
    match opcion.lower():
            case 'a':
                sustituirVocales()
                print("")
            case 'b':
                pedirNumeros()
                print("")
            case 'c':
                palabraMasLarga()
                print("")
            case 'e':
                contarCaracteres()
                print("")
            case 'f':
                print("Fin del programa")
                flag = True
            case _:
                print('No ha indicado ninguna de las opciones, ' \
                'inténtelo de nuevo: ')
                print("")
