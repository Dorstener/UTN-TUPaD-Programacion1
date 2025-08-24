#solicitamos al usuario el hemisferio en que se encuentra

hemis = str(input("En que hemisferio se encuentra. Por favor seleccione (Sur/Norte): ")).capitalize()

#solicitamos al usuario el mes y dia de la semana
print("Ingrese a continuación, el día (de hoy) y el mes (de hoy)")
dia = int(input("Dia: "))
mes = int(input("Mes (1/12): "))

# validamos primero el hemisferio, y en base al hemisferio seleccionado, indicamos al usuario la estación en la que se encuentra

if (hemis == "Sur"):
# Ahora validamos en que mes/dia se encuentra el usuario
    if(((mes == 12) and (dia >= 21)) or (mes == 1) or (mes == 2) or ((mes == 3) and (dia <= 20))):
        print("Te encuentras en Verano")
    elif (((mes == 3) and (dia >= 21)) or (mes == 4) or (mes == 5) or ((mes == 6) and (dia <= 20))):
        print("Te encuentras en Otonho")
    elif (((mes == 6) and (dia >= 21)) or (mes == 7) or (mes == 8) or ((mes == 9) and (dia <= 20))):
        print("Te encuentras en Invierno")
    elif (((mes == 9) and (dia >= 21)) or (mes == 10) or (mes == 11) or ((mes == 12) and (dia <= 20))):
        print("Te encuentras en Primavera")
elif (hemis == "Norte"):
# Ahora validamos en que mes/dia se encuentra el usuario
    if(((mes == 12) and (dia >= 21)) or (mes == 1) or (mes == 2) or ((mes == 3) and (dia <= 20))):
        print("Te encuentras en Invierno")
    elif (((mes == 3) and (dia >= 21)) or (mes == 4) or (mes == 5) or ((mes == 6) and (dia <= 20))):
        print("Te encuentras en Primavera")
    elif (((mes == 6) and (dia >= 21)) or (mes == 7) or (mes == 8) or ((mes == 9) and (dia <= 20))):
        print("Te encuentras en Verano")
    elif (((mes == 9) and (dia >= 21)) or (mes == 10) or (mes == 11) or ((mes == 12) and (dia <= 20))):
        print("Te encuentras en Otonho")
