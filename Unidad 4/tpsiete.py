# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Usuario dame un numero, campeon: "))

suma = 0

for x in range (0,num):
    suma = suma + x

print(suma)

