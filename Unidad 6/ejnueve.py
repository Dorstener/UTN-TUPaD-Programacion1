# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Definicion de Funcion

def celsius_a_fahrenheit(celsius):
    fahren = (celsius * 9/5) + 32
    print(f"{celsius} grados celsius convertido a Fahrenheit es: {fahren}")

# Programa Principal

celsius = float(input("Ingrese la temperatura que desea convertir: "))
celsius_a_fahrenheit(celsius)
