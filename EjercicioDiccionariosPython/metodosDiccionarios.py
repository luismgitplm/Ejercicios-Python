# ============================================
# MÉTODOS MÁS ÚTILES DE DICCIONARIOS EN PYTHON
# ============================================

# Diccionario de ejemplo
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}


# ------------------------------------------------
# get(clave, valor_por_defecto)
# Devuelve el valor asociado a una clave.
# Si la clave no existe, devuelve None o un valor por defecto.
edad = persona.get("edad")
pais = persona.get("pais", "España")

# Resultado esperado:
# edad = 30
# pais = "España"


# ------------------------------------------------
# keys()
# Devuelve una vista con todas las claves del diccionario.
claves = persona.keys()

# Resultado esperado:
# claves = dict_keys(["nombre", "edad", "ciudad"])


# ------------------------------------------------
# values()
# Devuelve una vista con todos los valores del diccionario.
valores = persona.values()

# Resultado esperado:
# valores = dict_values(["Ana", 30, "Madrid"])


# ------------------------------------------------
# items()
# Devuelve pares (clave, valor) del diccionario.
items = persona.items()

# Resultado esperado:
# items = dict_items([
#   ("nombre", "Ana"),
#   ("edad", 30),
#   ("ciudad", "Madrid")
# ])


# ------------------------------------------------
# update(diccionario)
# Actualiza el diccionario con los pares clave-valor de otro diccionario.
persona.update({"edad": 31, "profesion": "Ingeniera"})

# Resultado esperado:
# persona = {
#   "nombre": "Ana",
#   "edad": 31,
#   "ciudad": "Madrid",
#   "profesion": "Ingeniera"
# }


# ------------------------------------------------
# pop(clave)
# Elimina una clave y devuelve su valor.
ciudad = persona.pop("ciudad")

# Resultado esperado:
# ciudad = "Madrid"
# persona ya no contiene la clave "ciudad"


# ------------------------------------------------
# popitem()
# Elimina y devuelve el último par (clave, valor) insertado.
ultimo = persona.popitem()

# Resultado esperado:
# ultimo = ("profesion", "Ingeniera")


# ------------------------------------------------
# setdefault(clave, valor_por_defecto)
# Devuelve el valor de una clave; si no existe, la crea con un valor.
telefono = persona.setdefault("telefono", "000000000")

# Resultado esperado:
# telefono = "000000000"
# persona ahora contiene la clave "telefono"


# ------------------------------------------------
# clear()
# Elimina todos los elementos del diccionario.
copia = persona.copy()
copia.clear()

# Resultado esperado:
# copia = {}


# ------------------------------------------------
# copy()
# Crea una copia superficial del diccionario.
persona_copia = persona.copy()

# Resultado esperado:
# persona_copia contiene los mismos datos que persona
# pero es un objeto distinto


# ------------------------------------------------
# in (operador de pertenencia)
# Comprueba si una clave existe en el diccionario.
existe_nombre = "nombre" in persona
existe_pais = "pais" in persona

# Resultado esperado:
# existe_nombre = True
# existe_pais = False


# ------------------------------------------------
# del
# Elimina una clave del diccionario.
del persona["telefono"]

# Resultado esperado:
# persona ya no contiene la clave "telefono"
