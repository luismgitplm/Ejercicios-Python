'''8. # Ejercicio 13. Definir la función
# segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []'''
def segmento(inicio,final,lista):
    segmento = []
    if inicio < final:
        try:
            for i in range(inicio - 1, final):
                segmento.append(lista[i])
        except IndexError:
            print("Posiciones indicadas fuera del alcance de la lista.")
    
    return segmento

print(segmento(3,5,[3,4,1,2,7,9,0]))
