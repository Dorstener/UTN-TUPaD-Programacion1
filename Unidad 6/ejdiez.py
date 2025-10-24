# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


# Definicion de funciones

def calcular_promedio(a,b,c):
    suma = a + b + c 
    prom = suma / 3
    print(f"El promedio de los números ingresados es: {prom:.2f}")

# Programa Principal

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un segundo número: "))
num3 = float(input("Ingrese un tercer número: "))
calcular_promedio(num1,num2,num3)