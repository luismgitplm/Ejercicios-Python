'''10. Las dimensiones de los rectángulos puede representarse
# por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y
# altura 3.
#
# Definir la función
# mayorRectangulo : (tuple[float, float], tuple[float, float])
# -> tuple[float, float]
# tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre
# r1 y r2. Por ejemplo,
# mayorRectangulo((4, 6), (3, 7)) == (4, 6)
# mayorRectangulo((4, 6), (3, 8)) == (4, 6)
# mayorRectangulo((4, 6), (3, 9)) == (3, 9)'''
def esTuplaNumerica(*tuplas):
    return all(
        isinstance(tupla, (tuple)) 
        and all(isinstance(num, (int,float)) for num in tupla) 
        for tupla in tuplas)

def mayorRectangulo(r1,r2):
    if not esTuplaNumerica(r1,r2) or len(r1) != 2 or len(r2) != 2:
        print("Debe indicar dos tuplas numéricas con dos valores.")
    else:
        area_r1 = r1[0] * r1[1]
        area_r2 = r2[0] * r2[1]
        return r1 if area_r1 >= area_r2 else r2

print(mayorRectangulo((4,6),(3,7)))
print(mayorRectangulo((4,6),(3,8)))
print(mayorRectangulo((4,6),(3,9)))
print(mayorRectangulo((4,6,2),(3,8)))
print(mayorRectangulo('a',(3,8)))

