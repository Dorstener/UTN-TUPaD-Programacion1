# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Solicitamos al usuario su edad
edad = int(input("Ingrese su edad: "))

# Comparamos la edad del usuario, si es mayor o igual a 18, va a indicar que es mayoor de edad
if (edad >= 18):
    print("Es mayor de edad")

# Si no lo es, entonces va a mostrar que es menor de edad
else:
    print("Es menor de edad")