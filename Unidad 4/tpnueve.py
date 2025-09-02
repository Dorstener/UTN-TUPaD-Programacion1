# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

num = 0
sum = 0
cant_num_ingresado = 0
media = 0

for x in range (0,101):
    num = int(input("Ingresa un numero campeon: "))
    cant_num_ingresado = cant_num_ingresado + 1
    sum = num + sum

media = (sum/cant_num_ingresado)

print(sum)
print(cant_num_ingresado)
print(f"La media de todos los numeros ingresados es de {media}")