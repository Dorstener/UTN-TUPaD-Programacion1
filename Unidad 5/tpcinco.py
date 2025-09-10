# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.


estu_presentes = ["Panchito", "Horacio", "Hernan", "Fer", "Eugenio", "Narigon", "Cabezon", "Seba"]


accion = input("Desea agregar o eliminar a un estudiante de la lista?: (agregar/eliminar) ")

if accion == "agregar":
    estu_presentes.append(input(str("Ingrese el nombre del estudiante a agregar: ")))
else:
    estu_presentes.remove(input(str("Ingrese el nombre del estudiante a eliminar: ")))

print(estu_presentes)