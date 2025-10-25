# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("Lunes", "9:00"): "Welcome Meeting",
    ("Martes", "9:00"): "Intro a la programacion",
    ("Miercoles", "9:00"): "Desafios del Aprendizaje",
    ("Jueves", "9:00"): "Live Coding Session",
    ("Viernes", "18:00"): "Cierre de Evento",
    }

dia = input("Ingrese el dia del evento: ")
hora = input("Ingrese el horario del evento: ")

if (dia,hora) in agenda:
    print(f"El {dia} a las {hora} tiene el evento: {agenda[(dia,hora)]}")
else:
    print("NO hay eventos programados para ese dia/hora")