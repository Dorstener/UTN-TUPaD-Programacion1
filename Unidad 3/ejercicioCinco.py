# Objetivo: Clasificar temperaturas en rangos.
# Instrucciones:
# 1. Pide la temperatura actual en °C.
# 2. Si es ≤ 10°C, imprime: "Hace frío".
# 3. Si está entre 10°C y 25°C, imprime: "Está templado".
# 4. Si es > 25°C, imprime: "Hace calor".

temp = float(input("Ingrese la temperatura actual en Celsius: "))

if (temp <= 10):
    print("Hace frío")
elif (temp >= 10 and temp <= 25):
    print("Está templado")
else:
    print("Hace calor")


# Preguntas de reflexión:
# 1) ¿Cómo adaptarías el programa para usar °F?
# Una vez ingresado el valor en celsius, lo convertiría a Fahrenheit. Y mismo convertiría a fahrenheit todos los valores dentro de los operadores relacionales 

# 2) ¿Qué considerarías para añadir más rangos (ej: "Hace mucho frío")?
# Agregaría un operador relacional mas, donde si (temp < 0) > print("Hace mucho frío")