"""8. Escribe un programa que recoja un mes del año (en número) y devuelva el
número de días que tiene el mes. En caso de indicar un mes incorrecto deberá
mostrar un mensaje de error."""
mes = int(input("Indique un mes en número (del 1 al 12)"))

match mes:
    case 1,3,5,7,8,10,12:
        print("El mes tiene 31 días")
    case 4,6,9,11:
        print("El mes tiene 30 días")
    case 2:
        print("El mes tiene 28 días")
    case _:
        print("El número indicado no coincide con ningúm mes")
