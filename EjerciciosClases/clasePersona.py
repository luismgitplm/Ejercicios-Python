class Persona:
    def _init_(self,nombre,direccion,telefono):
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

def mostrarOrdenAlfabetico():
    ordenado = {clave : contactos[clave] for clave in sorted(contactos.keys())}

    print("Lista de contactos ordenada alfabéticamente:")

    for clave,contacto in ordenado.items():
        print(f"{clave}:\n  Nombre: {contacto.getNombre()}\n  Dirección: {contacto.getDireccion()}\n  Teléfono: {contacto.getTelefono()}\n")

def anyadirContacto():
    nombre = input("Indique el nombre:")
    direccion = input("Indique la direccion:")
    telefono = input("Indique el telefono:")

    contacto = Persona(nombre,direccion,telefono)
    
    if nombre.upper() not in contactos or input("El contacto ya existe, desea actualizarlo con el teléfono indicado?") == "si":
        contactos[nombre.upper()] = contacto
        print("Se ha actualizado la lista de contactos")
    else:
        print("No se ha actualizado la lista de contactos")

def modificarContacto():
    nombre = input("Indique el nombre del contacto:")

    if nombre.upper() in contactos or input("El contacto no existe, ¿desea insertarlo?") == "si":
        direccion = input("Indique la dirección:")
        telefono = input("Indique el teléfono:")
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


    

    

        

