# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese su frase favorita: ")
palabras_separadas = frase.split()
set(palabras_separadas)
conteo = {}

for palabra in palabras_separadas:
    if palabra in conteo:
        conteo[palabra] = conteo[palabra] + 1 
    else:
        conteo[palabra] = 1

print(conteo)