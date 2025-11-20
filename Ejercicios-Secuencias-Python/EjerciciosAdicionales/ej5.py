'''5. Definir la función
# rango : (List[int]) -> List[int]
# tal que rango(xs) es la lista formada por el menor y mayor elemento
# de xs.
# rango([3, 2, 7, 5]) == [2, 7]'''
def rango(lista):
    maximo = max(lista)
    minimo = min(lista)
    listaRango = [minimo,maximo]

    return listaRango

print(rango([3,2,7,5]))