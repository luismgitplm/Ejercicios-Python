"""4. Escribe un programa que recoja dividendo y divisor, y realice su división
siempre que el divisor sea distinto de cero."""
dividendo = int(input("Indique un número entero como dividendo:"))
divisor = int(input("Indique un segundo número entero como divisor:"))

if divisor != 0:
    print(f"La división de ambos números es {dividendo/divisor}")
else:
    print("Al ser el segundo número indicado cero, no puede ser el divisor del primer número.")