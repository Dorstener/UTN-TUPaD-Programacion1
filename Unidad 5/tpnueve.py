# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.


tateti = [
    ["-","-","-",],
    ["-","-","-",],
    ["-","-","-",],
]

jug_fila = 0 
jug_col = 0
fila = 0
col = 0

for fila in tateti:
    jug_fila = int(input("Jugador Uno, seleccione en que fila desea poner su ficha: 1/2/3: "))
    jug_col = input("Jugador Uno, seleccione en que columna desea poner su ficha: (Izquierda / Centro / Derecha): ")
    
    if jug_fila == 1 and jug_col == "Izquierda":
        tateti[0][0] = "X"
    elif jug_fila == 1 and jug_col == "Centro":
        tateti[0][1] = "X"
    elif jug_fila == 1 and jug_col == "Derecha":
        tateti[0][2] = "X"
    elif jug_fila == 2 and jug_col == "Izquierda":
        tateti[1][0] = "X"
    elif jug_fila == 2 and jug_col == "Centro":
        tateti[1][1] = "X"
    elif jug_fila == 2 and jug_col == "Derecha":
        tateti[1][2] = "X"
    elif jug_fila == 3 and jug_col == "Izquierda":
        tateti[2][0] = "X"
    elif jug_fila == 3 and jug_col == "Centro":
        tateti[2][1] = "X"
    elif jug_fila == 3 and jug_col == "Derecha":
        tateti[2][2] = "X"

    jug_fila = int(input("Jugador Dos, seleccione en que fila desea poner su ficha: 1/2/3: "))
    jug_col = input("Jugador Dos, seleccione en que columna desea poner su ficha: (Izquierda / Centro / Derecha): ")
    
    if jug_fila == 1 and jug_col == "Izquierda":
        tateti[0][0] = "O"
    elif jug_fila == 1 and jug_col == "Centro":
        tateti[0][1] = "O"
    elif jug_fila == 1 and jug_col == "Derecha":
        tateti[0][2] = "O"
    elif jug_fila == 2 and jug_col == "Izquierda":
        tateti[1][0] = "O"
    elif jug_fila == 2 and jug_col == "Centro":
        tateti[1][1] = "O"
    elif jug_fila == 2 and jug_col == "Derecha":
        tateti[1][2] = "O"
    elif jug_fila == 3 and jug_col == "Izquierda":
        tateti[2][0] = "O"
    elif jug_fila == 3 and jug_col == "Centro":
        tateti[2][1] = "O"
    elif jug_fila == 3 and jug_col == "Derecha":
        tateti[2][2] = "O"
        
    for fila in tateti:
        for elemento in fila:
            print(elemento, end=" ")
        print()