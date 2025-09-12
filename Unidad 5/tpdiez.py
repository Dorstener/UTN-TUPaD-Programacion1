# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.


ventas = [
    ["Manzanas",25,20,67,87,57,44,39],
    ["Naranjas",36,9,74,58,67,49,84],
    ["Peras",12,16,64,47,38,74,58],
    ["Uva",40,41,21,24,70,84,54],
]

ventas_total = 0
dias = [0,0,0,0,0,0,0]
nombres =["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]


for fila in ventas:
    ventas_total = fila[1] + fila[2] + fila[3] + fila[4] + fila[5] + fila[6] + fila[7]
    print(f"El total de {fila[0]} vendidas esta semana es de: {ventas_total}")
    for i in range(7):
        dias[i] = dias[i] + fila[i+1]
max_total = max(dias)
print(dias)
print(f"El dia que mas se vendio, se vendieron un total de {max_total} productos")





