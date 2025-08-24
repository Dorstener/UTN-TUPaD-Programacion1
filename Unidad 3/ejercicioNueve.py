# Ejercicio 9: Mejorando mensajes de error
# Objetivo: Dar retroalimentación específica al usuario.
# Instrucciones:
# 1. Basado en el Ejercicio 8, mejora los mensajes de error:
# > Si tiene <8 caracteres: "La contraseña no es segura. Debe tener al menos 8 caracteres.".
# > Si tiene >20 caracteres: "...no más de 20 caracteres.".
# > Si falta mayúscula: "...al menos una mayúscula.".
# > Si falta número: "...al menos un número.".

contrasena = str(input("Ingrese una contrasena: "))

longitud_valida = (len(contrasena) >= 8) and (len(contrasena) <= 20)
tiene_mayuscula = any(c.isupper() for c in contrasena)
tiene_numero = any(c.isdigit() for c in contrasena)

if ((len(contrasena) < 8) and tiene_mayuscula and tiene_numero):
    print("La contraseña no es segura. Debe tener al menos 8 caracteres")
elif ((len(contrasena) > 20) and tiene_mayuscula and tiene_numero):
    print("La contraseña no es segura. No debe tener mas de 20 caracteres")
elif (not(tiene_mayuscula) and longitud_valida and tiene_numero):
    print("La contraseña no es segura. Debe tener al menos una mayúscula.")
elif (not(tiene_numero) and longitud_valida and tiene_mayuscula):
    print("La contraseña no es segura. Debe tener al menos un número")
else:
    print("Felicitaciones!. Creaste tu contrasena")




# Preguntas de reflexión:
# 1. ¿Cómo evitarías repetir código al verificar cada condición?
# Honestamente, no se como prodría reducir las validaciones, sobre todo porque no es comprobar si alguna de las 3 condiciones (mayusculas, longitud o numero), sino que ademas de comprar cada una de las tres, tambien hay que mostrar un mensaje de error especifico
# 2. ¿Qué ventajas tiene este enfoque para el usuario?