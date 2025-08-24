contrasena_correcta = "programacion1"

# Le pedimos al usuario que ingrese la contrasenha
contrasena_usuario = input("Introduce la contraseña: ")

# Comparamos la "contrasenha del usuario" con la "contrasenha correcta" y si es correcta se muestra el resultado positivo, sino, se le informa que es incorrecta
if contrasena_usuario == contrasena_correcta:
    print("Contraseña correcta. Bienvenido.")
else: 
    print("Contraseña incorrecta. Intenta de nuevo.")


# 1) ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas? > La contrasenha es considerada incorrecta, porque solo se acepta en miniscula
# 2) ¿Cómo mejorarías el programa para dar más intentos? Agregaria un while

contrasena_correcta = "programacion1"
intentos = 5

while intentos > 0:
    contrasena_usuario = input("Introduce la contraseña: ")
    if contrasena_usuario == contrasena_correcta:
        print("Contraseña correcta. Bienvenido.")
    else: 
        intentos = intentos - 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
        print(intentos)
if intentos == 0:
    print("Se han agotado tus intentos. Tu cuenta se ha bloqueado. Contacta al administrador")

    