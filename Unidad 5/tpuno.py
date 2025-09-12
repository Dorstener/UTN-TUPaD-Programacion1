# Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [7,8,9.5,7.5,8,10,4,6,2,9]

suma_notas = sum(notas)
cant_notas = (len(notas))
promedio = (suma_notas/cant_notas)
nota_alta = notas[0]
nota_baja = notas[0]

print(f"El listado total de notas de los 10 estudiantes es el siguiente: {notas}")
print(f"El promedio entre las notas de los 10 estudiantes es de: {promedio}")

for nota in notas:
    if (nota > nota_alta):
        nota_alta = nota
    elif (nota < nota_baja):
        nota_baja = nota
        
print(f"La nota mas alta obtenida por un alumno es de: {nota_alta}")
print(f"La nota mas baja obtenida por un alumno es de: {nota_baja}")