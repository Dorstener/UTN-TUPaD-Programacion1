# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un numero: "))
num_digitos = len(str(num))
print(f"El numero ingresado tiene {num_digitos} digitos")

