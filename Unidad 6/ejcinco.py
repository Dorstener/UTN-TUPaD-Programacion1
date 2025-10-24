# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función


# Definicion de Funcion

def segundos_a_horas(segundos):
    horas = float(segundos / 3600)
    print(f"La cantidad de segundos ingresadors corresponde a {horas} horas")


# Programa Principal

segundos = int(input("Ingrese la cantidad de segundos que desea traducir a horas:  "))
segundos_a_horas(segundos)