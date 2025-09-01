# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.



num_uno = int(input("Ingrese un numero: "))
num_dos = int(input("Ingrese un segundo numero: "))

suma = 0

for x in range (num_uno + 1, num_dos):
    suma = suma + x

print(f"La suma de los números entre {num_uno} y {num_dos} es igual a ", suma)