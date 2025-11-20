#7. Escribe un programa que recoja la hora del día y devuelva un saludo.
import time
horaActual = int(time.strftime("%H", time.localtime()))

if (horaActual >= 7 and horaActual < 12):
    saludo = "Buenos días."
elif (horaActual >= 12 and horaActual < 20):
    saludo = "Buenas tardes."
else:
    saludo = "Buenas noches."

print(saludo)

