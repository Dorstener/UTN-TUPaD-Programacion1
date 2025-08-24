# Ejercicio 8: Validador de contraseña segura
# Objetivo: Implementar múltiples condiciones.
# Instrucciones:
# 1. Pide al usuario que cree una contraseña.
# 2. Verifica que cumpla:
# > 8+ caracteres y ≤20 caracteres.
# > Al menos 1 mayúscula (usa .isupper()).
# > Al menos 1 número (usa .isdigit()).
# 3. Si es segura, imprime: "¡Felicitaciones! Creaste tu contraseña.".
# 4. Si no, imprime: "La contraseña no es segura.".

contrasena = str(input("Ingrese una contrasena: "))

longitud_valida = (len(contrasena) >= 8) and (len(contrasena) <= 20)
tiene_mayuscula = any(c.isupper() for c in contrasena)
tiene_numero = any(c.isdigit() for c in contrasena)

if longitud_valida and tiene_mayuscula and tiene_numero:
    print("¡Felicitaciones! Creaste tu contraseña.")
else:
    print("La contraseña no es segura.")



# Preguntas de reflexión:
# 1) ¿Cómo añadirías la regla de usar un carácter especial?
# 2) ¿Por qué es importante limitar la longitud máxima?