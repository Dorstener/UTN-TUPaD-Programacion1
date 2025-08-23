# Ejercicio 2: Identificador de vocales
# Objetivo: Clasificar caracteres usando condicionales.
# Instrucciones:
# 1. Solicita una letra al usuario.
# 2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra ingresada es una vocal".
# 3. En otro caso, imprime: "La letra ingresada no es una vocal".


letra = input("Ingrese una letra: ")

if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada no es una vocal")


# Preguntas de reflexión:
# 1) ¿Cómo manejarías vocales acentuadas (á, é)?

# Opcion a) Las agregaría a la cadena de OR como en el ejercicio
# Opcion b) Agregaria un elif, donde si el usuario agrega vocales con acento le indique que vuelva a ingresar la vocal pero sin acento

# 2) ¿Qué estructura usarías para simplificar las comparaciones?

# Utilizaria el operador Switch