# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_usuario = int(input("Adivine el número mágico ingresando un número entre 0 y 9: "))

if num_usuario >= 10 or num_usuario < 0:
    print("El numero ingresado no se encuentra dentro de 0 y 9. Ingrese otro numero")
    num_usuario = int(input("Adivine el número mágico ingresando un número entre 0 y 9: "))

num_secreto = random.randint (0,9)
intentos = 1

while num_usuario != num_secreto:
    intentos = intentos + 1
    num_usuario = int(input("Adivine el número mágico ingresando su número: "))

print(f"El usuario necesito {intentos} intentos para adivinar el numero")