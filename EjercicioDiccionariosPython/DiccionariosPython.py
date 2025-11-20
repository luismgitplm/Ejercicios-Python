
contactos = {
    "Luis": 654789345,
    "Sara": 622333768,
    "Alfredo": 612345678,
    "Jaime": 673456128,
    "ben": 123456789
}

def mostrarDiccionario(d):
    for i in d.items():
        print(i)

def anyadirContacto(clave,valor):
    if clave not in contactos or input("Ese nombre ya existe, ¿desea actualizar? (si/no)").strip().lower() == 'si':
        contactos[clave] = valor
        print("Lista de contactos actualizada")
    else:
        print("Lista de contactos no actualizada")
    

def modificarContacto():
    clave = input("Indique el nombre del contacto: ")
    if clave in contactos or input("No se encuentra en la lista. ¿Desea insertar? (si/no): ").strip().lower() == 'si':
        contactos[clave] = int(input("Indique el número: "))
        print("Lista de contactos actualizada.")
    else:
        print("No se insertó el contacto.")

def buscarContacto(numero):
    if numero in contactos.values():
        for key,val in contactos.items():
            if val == numero:
                 print(key)
    else:
        print("El número no se encuentra en los contactos.")

def eliminarContacto(nombre):
    if nombre not in contactos:
        print("El nombre indicado no se encuentra en los contactos")
    else:
        del contactos[nombre]

def borrarTodo():
    opcion = input("¿Quiere eliminar todos los contactos? Escriba si o no ")
    if opcion.lower() == 'si':
        contactos.clear()


flag = False
while not flag:
    print("Escoja una opción:\n"\
    "a) Listado de teléfonos\n" \
    "b) Listado de teléfonos por orden alfabético\n" \
    "c) Añadir nuevo contacto\n" \
    "d) Modificar el teléfono de un contacto\n" \
    "e) Buscar número de teléfono\n" \
    "f) Eliminar contacto\n" \
    "g) Borrar toda la lista\n" \
    "h) Salir")
    print("")

    opcion = input()
    match opcion.lower():
        case 'a':
            print("El listado de contactos:")
            mostrarDiccionario(contactos)
            print("")
        case 'b':
            print("El listado de contactos por orden alfabético:")
            mostrarDiccionario(dict(sorted(contactos.items(), key = lambda x : x[0].lower())))
            print("")
        case 'c':
            clave = input("Indique el nombre: ")
            valor = int(input("Indique el número: "))
            anyadirContacto(clave,valor)
            print("")
        case 'd':
            modificarContacto()
            print("")
        case 'e':
            numero = int(input("Indique el número de teléfono: "))
            buscarContacto(numero)
            print("")
        case 'f':
            nombre = input("Indique el nombre que desea eliminar: ")
            eliminarContacto(nombre)
            print("")
        case 'g':
            borrarTodo()
            print("")
        case 'h':
            print("Fin del programa")
            flag = True
        case _:
            print('No ha indicado ninguna de las opciones, ' \
            'inténtelo de nuevo: ')
            print("")
