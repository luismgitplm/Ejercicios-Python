"""10.Escribe un programa que recoja la edad del usuario y muestre la edad que
tendrá dentro de 5, 10 y 15 años."""
edad = int(input("Indique su edad: "))

for i in range(5,16,5):
    print("Su edad dentro de {} años será: {}".format(i,edad+i))