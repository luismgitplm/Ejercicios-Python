"""3. La tienda "El Gran Bazar" desea analizar sus ventas diarias y mensuales. Tienes
un diccionario que contiene las ventas de cada producto para cada día del mes.
Cada producto tiene registrado cuántas unidades se vendieron en cada día del
mes."""

ventas = {
"A": {1: 5, 2: 3, 3: 6, 4: 8, 5: 1},
"B": {1: 3, 2: 7, 3: 2, 4: 0, 5: 4},
"C": {1: 6, 2: 4, 3: 3, 4: 5, 5: 2},
"D": {1: 0, 2: 2, 3: 1, 4: 3, 5: 0}
}

'Cálculo del total de unidades vendidas por cada producto'
def totalUnidadesPorProducto():
    ventasTotales = {}
    sumatorio = 0

    for producto,unidades in ventas.items():
        for i in unidades:
            sumatorio += unidades[i]
        ventasTotales[producto] = sumatorio
        sumatorio = 0
    
    return ventasTotales

'Identificar el producto con más y menos ventas'
valores = totalUnidadesPorProducto()
minimo = 100
maximo = 0
for i in valores:
    maximo = max(valores[i],maximo)
    minimo = min(valores[i],minimo)

    if valores[i] == maximo:
        productoMax = i
    
    if valores[i] == minimo:
        productoMin = i


'Mostrar las ventas diarias del producto más vendido'
for valor in ventas[productoMax].values():
    print(valor)

'Encontrar el día con la mayor venta para cada producto'
def mayorVentaPorProducto():
    mayoresDias = {}
    mayorVenta = 0
    
    for producto,datos in ventas.items():
        for i in datos:
            mayorVenta = max(mayorVenta,datos[i])
            if datos[i] == mayorVenta:
                mayoresDias[producto] = i
        mayorVenta = 0
    
    return mayoresDias


for i in mayorVentaPorProducto().items():
    print(i)


'''
def mayorVentaPorProducto():
    mayoresDias = {}
    mayoresVentas = {}
    mayorVenta = 0
    
    for producto,datos in ventas.items():
        for i in datos:
            mayorVenta = max(mayorVenta,datos[i])
        mayoresVentas[producto] = mayorVenta
        mayorVenta = 0
    
    for producto,datos in ventas.items():
        for dia, valor in datos.items():
            if valor == mayoresVentas[producto]:
                mayoresDias[producto] = dia
    
    return mayoresDias
    




'Identificar el producto con más y menos ventas'
valores = totalUnidadesPorProducto()
minimo = 100
maximo = 0
for val in valores.values():
    maximo = max(val,maximo)
    minimo = min(val,minimo)

for clave,valor in valores.items():
    if valor == maximo:
        productoMax = clave

    if valor == minimo:
        productoMin = clave
    
    
    
'''