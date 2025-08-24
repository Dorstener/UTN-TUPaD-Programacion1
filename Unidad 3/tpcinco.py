# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python

# Solicitamos al usuario una contrasenha
contrasena = str(input("Ingrese una contrasena: "))

# Validamos la contrasenha, calculando los caracteres que tiene usando la funcion len()

if (len(contrasena) >= 8) and (len(contrasena) <= 14):
    print("Ha ingresado una contrasena correcta")
else:
    print("Por favor, ingrese una contrasenha de entre 8 y 14 caracteres")
