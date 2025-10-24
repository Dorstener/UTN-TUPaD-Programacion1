# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

# Definicion de Funciones

def calcular_area_circulo(radio):
    pi = 3.14
    area = pi * radio **2
    print(f"El area del circulo es de {area}")

def calcular_perimetro_circulo(radio):
    pi = 3.14
    perimetro = 2 * pi * radio
    print(f"El perimetro del circulo es de {perimetro}")



# Programa Principal


radio = float(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)