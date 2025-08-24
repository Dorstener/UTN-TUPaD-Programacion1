# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje

#Le solicitamos al usuario que ingrese la nota que obtuvo en su examen
nota = float(input("Ingrese la nota de su examen: "))

# Comparamos la nota, para ver si aprobo o desaprobo.
# Si la nota es mayo o igual a 6, lo aprueba

if nota >= 6:
    print("Aprobado")

# si la nota es menor a 6, lo desaprueba

else:
    print("Desaprobado")