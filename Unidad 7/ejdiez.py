# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

diccionario_original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago de Chile",
    "Uruguay": "Montevideo",
    "Bolivia": "La Paz",
    "Paraguay": "Asuncion",
    "Brasil": "Brasilia",
    "Peru": "Lima"
}

diccionario_invertido = {}

for pais, capital in diccionario_original.items():
    diccionario_invertido[capital] = pais

print(diccionario_invertido)