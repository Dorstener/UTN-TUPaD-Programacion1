#Solicitamos al usuario su nombre

nombre = str(input("Ingrese su nombre: "))

# Mostramos las opciones al usuario

print("Marque una opcion en base a las siguientes posibilidades:")
print("Marque 1, si quiere su nombre en mayúsculas")
print("Marque 2, si quiere su nombre en minusculas")
print("Marque 3, si quiere su nombre con la primera letra en mayúscula")

# Le pedimos al usuario que ingrese una opción
opcion = int(input("Elija su opcion (1, 2, 3): "))

# si elije opcion uno, usamos el metodo .upper() para convertirlo todo a mayusculas
if (opcion == 1):
    print(nombre.upper())


# si elije opcion DOS, usamos el metodo .lower() para convertirlo todo a minusculas
elif (opcion == 2):
    print(nombre.lower())


# si elije opcion tres, usamos el metodo .capitalize() para convertir solo la primera letra a mayuscula y el resto a minusculas
elif (opcion == 3):
    print(nombre.capitalize())

