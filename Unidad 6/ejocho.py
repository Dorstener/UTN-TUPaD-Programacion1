# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.


# Definicion de Formula

def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    print(f"Su Indice de Masa Corporal es de {imc:.2f}")


# Programa Principal

peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
calcular_imc(peso, altura)