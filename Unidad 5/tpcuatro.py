#Dada una lista con valores repetidos:
# datos = [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]
nueva_lista = []


for x in datos:
    if x in nueva_lista:
        pass
    else:
        nueva_lista.append(x)


print(nueva_lista)