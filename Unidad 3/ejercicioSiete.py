# Ejercicio 7: Ajustador de frases
# Objetivo: Manipular strings con condicionales.
# Instrucciones:
# 1. Pide una frase o palabra al usuario
# 2. Si no termina en punto, añádelo al final.
# 3. Imprime el resultado.

frase = str(input("Ingrese su palabra o frase favorita: "))

frase = frase.rstrip()

if not frase.endswith("."):
    frase = frase + "."

print(f"Su palabra o frase favorita es: {frase}")


# Preguntas de reflexión:
# 1) ¿Cómo manejarías frases que terminan con espacios?
# utilizando el metodo rstrip, para poder eliminar espacios

# 2) ¿Qué otros caracteres de puntuación podrías considerar?
# Signo de pregunta, signo de admiración