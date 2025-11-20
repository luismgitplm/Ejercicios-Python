'''9. Definir la función
# extremos : (int, list[A]) -> list[A]
# tal que extremos(n, xs) es la lista formada por los n primeros
# elementos de xs y los n finales elementos de xs. Por ejemplo,
# extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]'''
def extremos(num,lista):
    extremos = []

    if not isinstance(num,int) or num > len(lista) / 2:
        print("El número indicado debe ser un entero menor que la mitad de la lista.")
    else:
        for i in range(num):
            extremos.insert(i,lista[i])
            extremos.append(lista[len(lista) - num + i])    
    
    return extremos

print(extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]))
        