# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_uno_aprobado = {"Nicolas", "Horacio", "Hernan", "Fernando", "Eugenio", "Sebastian", "Alvaro", "Martin", "Victor"}
parcial_dos_aprobado = {"Nicolas", "Francisco", "Juan Manuel", "Fernando", "Joaquin", "Sebastian", "Mariano", "Lolo", "Victor"}

al_menos_un_parcial_aprobado = parcial_uno_aprobado | parcial_dos_aprobado
print(f"Estos son los alumnos que aprobaron al menos un parcial: {al_menos_un_parcial_aprobado}")


solo_un_parcial_aprobado = parcial_uno_aprobado ^ parcial_dos_aprobado
print(f"Estos son los alumnos que aprobaron solo un parcial: {solo_un_parcial_aprobado}")

ambos_parciales_aprobados = parcial_uno_aprobado & parcial_dos_aprobado
print(f"Estos son los alumnos que aprobaron los dos parciales: {ambos_parciales_aprobados}")