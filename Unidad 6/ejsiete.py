# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

# Definicion de funciones

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b
    total = (suma, resta, multiplicar,dividir)
    print(total)




# Programa Principal

a = int(input("Ingrese un número: "))
b = int(input("Ingrese un segundo número: "))
operaciones_basicas(a,b)