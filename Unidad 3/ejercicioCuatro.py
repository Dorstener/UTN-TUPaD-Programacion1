# Ejercicio 4: Comparador de números
# Objetivo: Comparar dos números con condicionales.
# Instrucciones:
# 1. Solicita dos números al usuario.
# 2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
# 3. Si el primero es menor, imprime: "El primer número ingresado es menor".
# Si son iguales, imprime: "Los números ingresados son iguales".

num_uno = int(input("Ingrese un número: "))
num_dos = int(input("Ingrese un segundo número: "))

if (num_uno > num_dos):
    print("El primer número ingresado es mayor")
elif (num_uno < num_dos):
    print("El primer número ingresado es menor")
else:
    print("Los números ingresados son iguales")


# Preguntas de reflexión:
# 1) ¿Cómo modificarías el programa para comparar más de dos números
# Utilizaría operadores lógicos (OR) para conectar más expresiones


# 2) ¿Qué pasa si se ingresan valores no numéricos?
# Va a dar error, porque el data type de las variables esta indicado via el "int" para tomar números enteros