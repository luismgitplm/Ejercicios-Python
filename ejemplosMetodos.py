# ==================================================
# archivo: metodos_strings_y_listas.py
# ==================================================

# ======================
# MÉTODOS DE STRINGS
# ======================

# Convierte el texto a mayúsculas
# Crea un NUEVO string (los strings son inmutables)
texto = "hola mundo"
print(texto.upper())
# Output esperado: HOLA MUNDO


# Convierte el texto a minúsculas
# Crea un NUEVO string
texto = "HoLa MuNdO"
print(texto.lower())
# Output esperado: hola mundo


# Elimina espacios en blanco al inicio y al final
# Crea un NUEVO string
texto = "  hola  "
print(texto.strip())
# Output esperado: hola


# Reemplaza una subcadena por otra
# Crea un NUEVO string
texto = "hola mundo"
print(texto.replace("mundo", "Python"))
# Output esperado: hola Python


# Divide el string en una lista usando un separador
# Crea una NUEVA lista
texto = "rojo,verde,azul"
print(texto.split(","))
# Output esperado: ['rojo', 'verde', 'azul']


# Une los elementos de una lista en un string
# Crea un NUEVO string
colores = ["rojo", "verde", "azul"]
print("-".join(colores))
# Output esperado: rojo-verde-azul


# Comprueba si el string empieza por un texto
# No modifica el objeto, devuelve un booleano
texto = "python"
print(texto.startswith("py"))
# Output esperado: True


# Comprueba si el string termina por un texto
# No modifica el objeto, devuelve un booleano
texto = "python"
print(texto.endswith("on"))
# Output esperado: True


# Comprueba si el string contiene solo letras
# No modifica el objeto, devuelve un booleano
texto = "Python"
print(texto.isalpha())
# Output esperado: True


# Comprueba si el string contiene solo números
# No modifica el objeto, devuelve un booleano
texto = "12345"
print(texto.isdigit())
# Output esperado: True


# ======================
# MÉTODOS DE LISTAS
# ======================

# Añade un elemento al final de la lista
# MODIFICA la lista existente
lista = [1, 2, 3]
lista.append(4)
print(lista)
# Output esperado: [1, 2, 3, 4]


# Inserta un elemento en una posición concreta
# MODIFICA la lista existente
lista = [1, 2, 3]
lista.insert(1, 99)
print(lista)
# Output esperado: [1, 99, 2, 3]


# Elimina el primer elemento que coincide con el valor
# MODIFICA la lista existente
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)
# Output esperado: [1, 3, 2]


# Elimina y devuelve el elemento de una posición
# MODIFICA la lista existente
lista = [1, 2, 3]
valor = lista.pop(1)
print(lista, valor)
# Output esperado: [1, 3] 2


# Elimina todos los elementos de la lista
# MODIFICA la lista existente
lista = [1, 2, 3]
lista.clear()
print(lista)
# Output esperado: []


# Ordena la lista de menor a mayor
# MODIFICA la lista existente
lista = [3, 1, 2]
lista.sort()
print(lista)
# Output esperado: [1, 2, 3]


# Ordena la lista sin modificar la original
# CREA una nueva lista
lista = [3, 1, 2]
ordenada = sorted(lista)
print(ordenada)
# Output esperado: [1, 2, 3]


# Invierte el orden de los elementos
# MODIFICA la lista existente
lista = [1, 2, 3]
lista.reverse()
print(lista)
# Output esperado: [3, 2, 1]


# Cuenta cuántas veces aparece un elemento
# No modifica la lista, devuelve un entero
lista = [1, 2, 2, 3]
print(lista.count(2))
# Output esperado: 2


# Devuelve el índice de la primera aparición del elemento
# No modifica la lista, devuelve un entero
lista = [10, 20, 30]
print(lista.index(20))
# Output esperado: 1


# Crea una copia superficial de la lista
# CREA una nueva lista
lista = [1, 2, 3]
copia = lista.copy()
print(copia)
# Output esperado: [1, 2, 3]
