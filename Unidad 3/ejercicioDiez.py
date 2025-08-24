# Ejercicio 10: Piedra, papel o tijera
# Objetivo: Implementar lógica de juego con condicionales anidados.
# Instrucciones:
# 1. Pide al usuario las jugadas del Jugador 1 y Jugador 2 (piedra, papel o tijera).
# 2. Usa la tabla proporcionada para determinar el resultado (ganador oempate).
# 3. Imprime: "GANA JUGADOR 1", "GANA JUGADOR 2" o "EMPATE"


jug_uno = str(input("Jugador Uno, Ingrese su opción entre Piedra, Papel o Tijera: "))
jug_dos = str(input("Jugador Dos, Ingrese su opción entre Piedra, Papel o Tijera: "))

if ((jug_uno != "Piedra") and (jug_uno != "Papel") and (jug_uno != "Tijera")):
    print("Jugador 1, Haz ingresado una opción incorrecta")
elif ((jug_dos != "Piedra") and (jug_dos != "Papel") and (jug_dos != "Tijera")):
    print("Jugador 2, Haz ingresado una opción incorrecta")

if (jug_uno == "Piedra") and (jug_dos == "Piedra"):
    print("Empate")
elif (jug_uno == "Piedra") and (jug_dos == "Papel"):
    print("Gana Jugador 2")
elif (jug_uno == "Piedra") and (jug_dos == "Tijera"):
    print("Gana Jugador 1")
elif (jug_uno == "Papel") and (jug_dos == "Piedra"):
    print("Gana Jugador 1")
elif (jug_uno == "Papel") and (jug_dos == "Papel"):
    print("Empate")
elif (jug_uno == "Papel") and (jug_dos == "Tijera"):
    print("Gana Jugador 2")
elif (jug_uno == "Tijera") and (jug_dos == "Piedra"):
    print("Gana Jugador 2")
elif (jug_uno == "Tijera") and (jug_dos == "Papel"):
    print("Gana Jugador 1")
elif (jug_uno == "Tijera") and (jug_dos == "Tijera"):
    print("Empate")







# Preguntas de reflexión:
# 1. ¿Cómo manejarías entradas inválidas (ej: "piedra" mal escrito)?
# Hice unas validaciones en el ejercicio

# 2. ¿Qué estructura usarías para simplificar las comparaciones?
# Despues de hacer las validaciones, buscando informacion, encontré que se puede utilizar el metodo "not in" , asi que podría haber creado una variable opciones_validas, poner dentro las opciones ["Piedra", "Papel", "Tijera"], y si "not in", entonces mostrar el mensaje.