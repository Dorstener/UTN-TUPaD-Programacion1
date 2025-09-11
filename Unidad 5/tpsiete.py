# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

matriz = [
    ["Lunes",20,28],
    ["Martes",23,24],
    ["Miercoles",19,26],
    ["Jueves",17,28],
    ["Viernes",19,50],
    ["Sabado",21,40],
    ["Domingo",23,24],
]

suma_max = 0
suma_min = 0
cant_min = 0
prom_min = 0
prom_max = 0
amplitud = 0
max_amplitud = 0
fila = 0
dia = ""


for x in matriz:
    suma_min = suma_min + x[1]
    suma_max = suma_max + x[2]
    fila = fila + 1
    amplitud = x[2] - x[1]
    if amplitud > max_amplitud:
        max_amplitud = amplitud
        dia = x[0]


prom_min = (suma_min/fila)
print(f"El promedio de la temperatura mínimo en la semana fue de {round(prom_min,1)} grados")
prom_max = (suma_max/fila)
print(f"El promedio de la temperatura maxima en la semana fue de {round(prom_max,1)} grados")
print(f"El dia {dia} fue el que tuvo una amplitud de {round(max_amplitud,1)} grados, siendo la mayor de todas")