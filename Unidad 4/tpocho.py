#  Escribe un programa que permita al usuario ingresar 100 números enteros.
#  Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num = 0
par = 0
impar = 0
neg = 0
pos = 0

for x in range (0,101):
    num = int(input("Ingresa un numero: "))
    if num % 2 == 0: 
        par = par + 1
    else:
        impar = impar + 1
    if num >= 0:
        pos = pos + 1
    else:
        neg = neg + 1

print(f"El usuario ingreso {par} numeros que son par")
print(f"El usuario ingreso {impar} numeros que son impar")
print(f"El usuario ingreso {pos} numeros que son positivo")
print(f"El usuario ingreso {neg} numeros que son negativo")