# Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.


# Le pedimos al usuario que ingrese un numero par

num = int(input("Ingrese un numero par: "))

# Validamos si el número es par, usando el operador MOD, donde si el número tiene resto 0, va a indicar que es par

if num % 2 == 0:
    print("Ha ingresado un número par")

# si no es par, se lo informamos al usuario

else:
    print("Por favor, ingrese un nuero par")