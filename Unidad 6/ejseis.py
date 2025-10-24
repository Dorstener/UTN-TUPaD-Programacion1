# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definicion de Funcion

def tabla_multiplicar(numero):
    for i in range(1,11):
        multiplicar = numero*i
        print(f"{numero} multiplicado por {i} es igual a {multiplicar}")


# Programa Princial

numero = int(input("Ingresar un numero: "))
tabla_multiplicar(numero)