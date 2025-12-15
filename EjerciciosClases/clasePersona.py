class Persona:
    def __init__(self,nombre,direccion,telefono):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if not telefono.isdigit() or len(telefono) != 9:
            raise ValueError("El teléfono debe tener exactamente 9 números")
    
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
    
    def getTelefono(self):
        return self._telefono

    def getNombre(self):
        return self._nombre
    
    def getDireccion(self):
        return self._direccion


contactos = {}

def pedir_nombre():
    while True:
        nombre = input("Nombre: ")
        try:
            if not nombre.strip():
                raise ValueError
            return nombre
        except ValueError:
            print("El nombre no puede estar vacío")


def pedir_telefono():
    while True:
        telefono = input("Teléfono: ")
        try:
            if not telefono.isdigit() or len(telefono) != 9:
                raise ValueError
            return telefono
        except ValueError:
            print("El teléfono debe tener 9 dígitos")


def crear_persona():
    nombre = pedir_nombre()
    direccion = input("Dirección: ")
    telefono = pedir_telefono()
    return Persona(nombre, direccion, telefono)

    

def mostrarOrdenAlfabetico():
    ordenado = {clave : contactos[clave] for clave in sorted(contactos.keys())}

    print("Lista de contactos ordenada alfabéticamente:")

    for clave,contacto in ordenado.items():
        print(f"{clave}:\n  Nombre: {contacto.getNombre()}\n  Dirección: {contacto.getDireccion()}\n  Teléfono: {contacto.getTelefono()}\n")

def anyadirContacto():

    contacto = crear_persona()
    
    if contacto.getNombre().upper() not in contactos or input("El contacto ya existe, desea actualizarlo con el teléfono indicado?").strip().lower() in ("si", "sí"):
        contactos[contacto.getNombre().upper()] = contacto
        print("Se ha actualizado la lista de contactos")
    else:
        print("No se ha actualizado la lista de contactos")

def modificarContacto():
    nombre = input("Indique el nombre del contacto:")

    if nombre.upper() in contactos or input("El contacto no existe, ¿desea insertarlo?").strip().lower() in ("si", "sí"):
        direccion = input("Dirección: ")
        telefono = pedir_telefono()
        contactos[nombre.upper()] = Persona(nombre,direccion,telefono)
        print("Se modificó la lista de contactos")
    else:
        print("No se insertó el contacto")

def buscarTelefono():
    telefono = input("Indique el telefono a buscar:")
    encontrado = False

    for persona in contactos.values():
        if telefono == persona.getTelefono():
            encontrado = True
            print(f"El nombre del contacto es: {persona.getNombre()}")
    
    if not encontrado:
        print("No se encontró el contacto")


def eliminarContacto():
    nombre = input("Indique el nombre del contacto a eliminar:")

    try:
        del contactos[nombre.upper()]
    except KeyError:
        print("El contacto no se ha encontrado")

#Menú de opciones
flag = False
while not flag:
    print("Escoja una opción:\n"\
    "a) Listado de contactos por orden alfabético\n" \
    "b) Añadir un nuevo contacto\n" \
    "c) Modificar un contacto\n" \
    "d) Buscar un número de teléfono\n" \
    "e) Eliminar un contacto\n" \
    "f) Salir")
    print("")


    opcion = input("Indique una opción: a,b,c,d,e. escriba f para salir:")
    match opcion.lower():
            case 'a':
                mostrarOrdenAlfabetico()
                print("")
            case 'b':
                anyadirContacto()
                print("")
            case 'c':
                modificarContacto()
                print("")
            case 'd':
                buscarTelefono()
                print("")
            case 'e':
                eliminarContacto()
                print("")
            case 'f':
                print("Fin del programa")
                flag = True
            case _:
                print('No ha indicado ninguna de las opciones, ' \
                'inténtelo de nuevo: ')
                print("")


    

        

