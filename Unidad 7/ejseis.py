# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

nombre_alumno = ""
nota = 0
nota_alumno = () 

for i in range (3):
    nombre_alumno = input(f"Ingrese nombre del alumno {i+1}: ")
    suma = 0
    promedio = 0
    suma_notas = []
    for x in range (3):
        nota = float(input(f"Ingrese nota {x+1} del alumno: "))
        suma_notas.append(nota)
    nota_alumno = tuple(suma_notas)
    promedio = sum(nota_alumno) / len(nota_alumno)
    print(f"El promedio de {nombre_alumno} es de: {promedio:.2}")

