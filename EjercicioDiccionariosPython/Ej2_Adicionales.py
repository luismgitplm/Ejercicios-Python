
"2. Modificar el programa anterior para que pueda manejar varios nombres."

def pedirEntero(mensaje):
    while True:
        try:
            Valor = int(input(mensaje))
            break
        except ValueError:
            print("No ha indicado un número entero, inténtelo de nuevo: ")
    return Valor


def anyadirPersona(diccionario):
    nombre = input("Indique el nombre")
    diccionario[nombre] = {
        "Edad": pedirEntero("Indique la edad (número entero): "),
        "Direccion": input("Indique la dirección"),
        "Telefono": pedirEntero("Indique el número de teléfono (número entero): ")
    }

personas = {}

anyadirPersona(personas)
anyadirPersona(personas)

for nombre,datos in personas.items():
    print("Nombre: ", nombre)

    for i in datos:
        print(i + ":", datos[i])