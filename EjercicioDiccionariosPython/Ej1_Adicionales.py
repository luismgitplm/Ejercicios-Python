"""1. Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un diccionario. Después debe
mostrar por pantalla el mensaje <nombre> tiene <edad> años,
vive en <dirección> y su número de teléfono es
<teléfono>."""


def pedirEntero(mensaje):
    while True:
        try:
            Valor = int(input(mensaje))
            break
        except ValueError:
            print("No ha indicado un número entero, inténtelo de nuevo: ")
    return Valor

persona = {
    "Nombre" : input("Indique su nombre: "),
    "Edad" : pedirEntero("Indique su edad: ") ,
    "Direccion" : input("Indique su dirección: "),
    "Telefono" : pedirEntero("Indique su número de teléfono: ")
}

print(f"{persona["Nombre"]} tiene {persona["Edad"]} años, vive en {persona["Direccion"]} y su número de teléfono es {persona["Telefono"]}")



