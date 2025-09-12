# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

clase = [
    ["Nicolas", "AySo",8,"Programacion",10,"Matematicas",9],
    ["Hernan", "AySo",6,"Programacion",9,"Matematicas",5],
    ["Horacio", "AySo",7,"Programacion",10,"Matematicas",8],
    ["Fernando", "AySo",10,"Programacion",8,"Matematicas",10],
    ["Eugenio", "AySo",5,"Programacion",6,"Matematicas",4], 
]

suma = 0
materias = 3
estudiantes = 5
promedio = 0
ayso_tot = 0
prom_ayso = 0
programacion_tot = 0
prom_programacion = 0
mate_tot = 0
prom_mate = 0

for x in clase:
    suma = x[2] + x[4] + x[6]
    promedio = suma/materias
    print(f"El promedio de {x[0]} en las 3 materias cursadas es de {round(promedio,1)}")
    ayso_tot = ayso_tot + x[2]
    programacion_tot = programacion_tot + x[4]
    mate_tot = mate_tot + x[6] 
    
    

prom_ayso = (ayso_tot/estudiantes)
print(f"El promedio de todos los estudiantes en la materia Arquitectura y Sistemas Operativos es: {prom_ayso}")
prom_programacion = (programacion_tot/estudiantes)
print(f"El promedio de todos los estudiantes en la materia Programación es: {prom_programacion}")
prom_mate = (mate_tot/estudiantes)
print(f"El promedio de todos los estudiantes en la materia Matemáticas es: {prom_mate}")
