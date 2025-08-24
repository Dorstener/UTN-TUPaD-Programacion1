# Solicitamos al usuario la magnitud del terremoto

magni = float(input("Ingrese la magnitud del terremoto segun la escala Richter: "))

# comparamos la magnitud ingresada

if (magni < 3):
    print("Muy Leve")
elif (magni >= 3) and (magni < 4):
    print("Leve")
elif (magni >= 4) and (magni < 5):
    print("Moderado")
elif (magni >= 5) and (magni < 6):
    print("Fuerte")
elif (magni >= 6) and (magni < 7):
    print("Muy Fuerte")
elif (magni >= 7):
    print("Extremo")