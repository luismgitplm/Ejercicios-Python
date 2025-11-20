'''7. # Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]'''
def finales(num,lista):
    copia = lista
    finales = []

    for _ in range(num):
        finales.insert(0,copia.pop())
    
    return finales

print(finales(3,[2,5,4,7,9,6]))