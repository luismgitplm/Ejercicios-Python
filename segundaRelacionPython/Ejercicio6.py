"""6. Escribe un programa que muestre la nota final de un alumno a partir de su
calificación numérica (valor decimal), teniendo en cuenta que:
a. Nota menor de 5 es suspenso.
b. Nota entre 5 y 6 (sin llegar) es suficiente.
c. Nota entre 6 y 7 (sin llegar) es bien.
d. Nota entre 7 y 9 (sin llegar) es notable.
e. Nota entre 9 y 10 (sin llegar) es sobresaliente.
f. Nota igual a 10 es matrícula de honor.
g. Cualquier otro valor numérico fuera de este rango es un error."""
calificacion = float(input("Indique su calificación numérica:"))

if calificacion < 5:
    print("Suspenso")
elif calificacion >= 5 and calificacion < 6:
    print("suficiente")
elif calificacion >= 6 and calificacion < 7:
    print("Bien")
elif calificacion >=7 and calificacion < 9:
    print("Notable")
elif calificacion >=9 and calificacion < 10:
    print("Sobresaliente")
else:
    print("Matrícula de honor")