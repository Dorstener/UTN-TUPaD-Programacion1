# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = int(input("Ingrese un numero: "))
suma = 0

while num != 0:
    suma = num + suma
    num = int(input("Ingrese otro número: "))

print(f"La suma total es: {suma}")