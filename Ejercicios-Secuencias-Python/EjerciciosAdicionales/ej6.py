'''6. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]'''
def interior(lista):
    modificacion = lista
    modificacion.pop(0)
    modificacion.pop()
    
    return modificacion

print(interior([2,5,3,7,3]))