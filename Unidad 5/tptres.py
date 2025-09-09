# Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

pares = []
impares = []
numero = 0

for x in range(5):
    num = random.randint(1,100)
    print(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"En esta lista estan reflejados todos los numeros impares generados aleatoriamente: {impares} ")
print(f"En esta lista estan reflejados todos los numeros pares generados aleatoriamente: {pares} ")

cant = 0
for x in impares:
    cant = cant + 1
print(f"La lista de numeros impares tiene {cant} numeros")

cantidad = 0
for x in pares:
    cantidad = cantidad + 1
print(f"La lista de numeros pares tiene {cantidad} numeros")