class Material:
    def __init__(self,id,titulo,autor,anyoPublicacion):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anyoPublicacion = anyoPublicacion


class Libro(Material):
    def __init__(self,id,titulo,autor,anyoPublicacion,genero,numPaginas):
        super().__init__(id,titulo,autor,anyoPublicacion)

        self.genero = genero
        self.numPaginas = numPaginas
    
    def getNumPaginas(self):
        return self.numPaginas
        
    
    def toString(self):
        print(f"Identificador: {self.id}\n  Título: {self.titulo}\n  Autor: {self.autor}\n  Año de publicación: {self.anyoPublicacion}\n  Género: {self.genero}\n  Número de páginas: {self.numPaginas}\n")



class Revista(Material):
    def __init__(self,id,titulo,autor,anyoPublicacion,numEdicion,mesPublicacion):
        super().__init__(id,titulo,autor,anyoPublicacion)

        self.numEdicion = numEdicion
        self.mesPublicacion = mesPublicacion
    
    def toString(self):
        print(f"Identificador: {self.id}\n  Título: {self.titulo}\n  Autor: {self.autor}\n  Año de publicación: {self.anyoPublicacion}\n  Número de edición: {self.numEdicion}\n  Mes de publicación: {self.mesPublicacion}\n")


#Función que controla excepciones para pedir números enteros
def pedirEntero(mensaje):
    while True:
        try:
            Valor = int(input(mensaje))
            break
        except ValueError:
            print("No ha indicado un número entero, inténtelo de nuevo: ")
    return Valor

#Diccionario que guarda todos los objetos revista y libro creados
materiales = {}

#Función que agrega un objeto libro al diccionario pidiendo los atributos
def agregarLibro():
    while True:
        id = pedirEntero("Indique el id:")

        if id in materiales:
            print("El id está repetido, indique otro")
        else:
            break
    
    while True:
        titulo = input("Indique el título: ")

        if not titulo.strip():
            print("El nombre no debe quedar vacío")
        else:
            break
    
    
    autor = input("Indique el autor: ")

    while True:
        anyoPublicacion = pedirEntero("Indique el año de publicación")

        if anyoPublicacion < 0:
            print("El año de publicación no puede ser negativo, escriba otro")
        elif anyoPublicacion > 2025:
            print("El año de publicación no puede ser mayor al actual, escriba otro")
        else:
            break
    
    while True:
        genero = input("Indique el género (Ficción, No ficción, Terror, Ciencia): ").strip().lower()

        if genero not in ("ficción","ficcion","no ficcion","no ficción","terror","ciencia"):
            print("El género debe ser uno de los siguientes: Ficción, No ficción, Terror, Ciencia")
        else:
            break
    
    while True:
        numPaginas = pedirEntero("Indique el número de páginas: ")

        if numPaginas < 0:
            print("El número de páginas no puede ser negativo, indíquelo de nuevo: ")
        else:
            break
    
    materiales[id] = Libro(id,titulo,autor,anyoPublicacion,genero,numPaginas)
    


#Función que agrega un objeto revista al diccionario pidiendo los atributos
def agregarRevista():
    while True:
        id = pedirEntero("Indique el id:")

        if id in materiales:
            print("El id está repetido, indique otro")
        else:
            break
    
    while True:
        titulo = input("Indique el título: ")

        if not titulo.strip():
            print("El nombre no debe quedar vacío")
        else:
            break
    
    
    autor = input("Indique el autor: ")

    while True:
        anyoPublicacion = pedirEntero("Indique el año de publicación")

        if anyoPublicacion < 0:
            print("El año de publicación no puede ser negativo, escriba otro")
        elif anyoPublicacion > 2025:
            print("El año de publicación no puede ser mayor al actual, escriba otro")
        else:
            break
    
    while True:
        numEdicion = pedirEntero("Indique el número de edición: ")

        if numEdicion <= 0:
            print("El número de edición no puede ser negativo ni cero, indíquelo de nuevo: ")
        else:
            break
    
    while True:
        mesPublicacion = input("Indique el mes de publicación (Nombre del mes): ").strip().lower()

        if mesPublicacion not in ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"):
            print("El mes de publicación debe ser el nombre en español de uno de los doce meses, indíquelo de nuevo: ")
        else:
            break
    
    materiales[id] = Revista(id,titulo,autor,anyoPublicacion,numEdicion,mesPublicacion)
    


    

#Función que da a elegir la opción de agregar un nuevo libro o una nueva revista
def agregarMaterial():

    while True:
        opcion = input("¿Qué material desea añadir? ¿Libro o Revista?").strip().lower()
        if opcion == "libro":
            agregarLibro()
            break
        elif opcion == "revista":
            agregarRevista()
            break
        else:
            print("Debe escribir o bien Libro o bien Revista, inténtelo de nuevo:")

#Función que muestra el estado de todos los materiales del diccionario
def listarMateriales():
    print("Todos los materiales agregados: \n")

    for material in materiales.values():
        material.toString()

#Función que pide un id y busca un material que lo contenga en caso de que exista
def buscarPorId():
    idABuscar = pedirEntero("Indique el id a buscar: ")

    if idABuscar not in materiales:
        print("Ningún material tiene asignado el id indicado")
    else:
        print("El material encontrado es: \n")
        materiales[idABuscar].toString()


#Función que pide un id y busca un material que lo contenga en caso de que exista para eliminarlo
def eliminarMaterial():
    idAEliminar = pedirEntero("Indique el id del material a eliminar: ")

    if idAEliminar not in materiales:
        print("Ningúm material tiene asignado el id indicado")
    else:
        print("Eliminando el material indicado...")
        del materiales[idAEliminar]


#Función que calcula y muestra las estadísticas totales
def mostrarEstadisticas():
    numeroLibros = 0
    numeroRevistas = 0
    totalPaginas = 0
    promedioPaginas = 0

    for material in materiales.values():
        if isinstance(material,Libro):
            numeroLibros += 1
            totalPaginas += material.getNumPaginas()
        else:
            numeroRevistas += 1
    
    promedioPaginas = totalPaginas / numeroLibros

    print("Las estadísticas totales: \n")
    print(f"Total de materiales: {numeroLibros + numeroRevistas}\n")
    print(f"Total de libros: {numeroLibros}\n")
    print(f"Total de revistas: {numeroRevistas}\n")
    print(f"Promedio de páginas de los libros: {promedioPaginas}\n")


#Menú de opciones
flag = False
while not flag:
    print("Escoja una opción:\n"\
    "a) Agregar material\n" \
    "b) Listar materiales\n" \
    "c) Buscar material mediante su id\n" \
    "d) Eliminar material\n" \
    "e) Generar estadísticas\n" \
    "f) Salir")
    print("")


    opcion = input("Indique una opción: a,b,c,d,e. escriba f para salir:")
    match opcion.strip().lower():
            case 'a':
                agregarMaterial()
                print("")
            case 'b':
                listarMateriales()
                print("")
            case 'c':
                buscarPorId()
                print("")
            case 'd':
                eliminarMaterial()
                print("")
            case 'e':
                mostrarEstadisticas()
                print("")
            case 'f':
                print("Fin del programa")
                flag = True
            case _:
                print('No ha indicado ninguna de las opciones, ' \
                'inténtelo de nuevo: ')
                print("")