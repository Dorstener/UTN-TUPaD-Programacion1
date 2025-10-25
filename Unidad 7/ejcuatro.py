# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.


contactos = {}

for i in range (0,5):
    nombre = str(input("Ingrese el nombre del contacto: "))
    telefono = int(input("Ingrese el telefono del contacto: "))
    contactos[nombre] = telefono

preg = input("Ingrese el nombre del contacto para visualizar su telefono: ")

if preg in contactos:
    print("El número de telefono de ", preg, "es: ", contactos[preg])
else:
    print("Ese contacto no existe en la agenda")


