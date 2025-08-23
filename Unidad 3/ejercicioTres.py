# Ejercicio 3: Clasificador de números
# Objetivo: Determinar el signo de un número.
# Instrucciones:
# 1. Pide un número al usuario.
# 2. Si es positivo, imprime: "El número es positivo".
# 3. Si es negativo, imprime: "El número es negativo".
# 4. Si es cero, imprime: "El número es cero".

num = int(input("Ingrese un numero: "))

if (num > 0):
    print("El número es positivo")
elif (num < 0):
    print("El número es negativo")
else:
    print("El número es igual a cero")


# Preguntas de reflexión:
# 1) ¿Qué ocurre si el usuario ingresa un texto?
# Va a dar error, porque en el pedido al usuario de que ingrese un numero, indique via el "int" el tipo de dato de la variable num, sea numéro entero

# • ¿Cómo adaptarías el código para números decimales?
# 2) Modificaría el data type de "int" a "float"