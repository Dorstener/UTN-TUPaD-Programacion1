# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Definicion de Funcion

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


# Programa Principal


saludar_usuario(nombre = input("Ingresa tu nombre: "))