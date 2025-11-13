# Actividad 5.Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

print("_"*40, "\n")
print(f"Actividad 5\n")
print("¡Hola!\n")

# Para poder limpiar la cadena de texto, sin tildes, se importará unicodedata
import unicodedata

# Función para limpar texto, se eliminarán espacios y tildes 
def limpiar_texto(texto):
    texto=texto.strip().lower()
    texto="".join(texto.split()) #Elimina espacios internos o saltos
    texto=unicodedata.normalize("NFD",texto) #Para separar letras de los acentos o similares
    texto="".join(letra for letra in texto if unicodedata.category(letra) != 'Mn') #para unir quitando acentos
    return texto

# Función que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo 
# o False si no lo es
def es_palindromo(palabra):
    palabra_limpia=limpiar_texto(palabra)
    longitud=len(palabra_limpia)
    #Por si quedó una cadena vacía luego de limpiar y en caso de que haya un sólo caracter
    if longitud<=1: 
        #Por definición de Palídromo, si está vacía o tiene un sólo caracter es palíndromo
        return True
    if palabra_limpia[0]!=palabra_limpia[-1]:
        return False
    #De forma recursiva recorta los extremos de la cadena de texto
    return es_palindromo(palabra_limpia[1:-1]) 

print("¿Es Palíndromo?\n")
print(f"1.-     : {es_palindromo("    ")}")
print(f"2.- a: {es_palindromo("a")}")
print(f"3.-    b    : {es_palindromo("   b    ")}")
print(f"4.- Reconocer: {es_palindromo("Reconocer")}")
print(f"5.-   AÉREOpuerto   : {es_palindromo("   AÉREOpuerto   ")}")
print(f"6.-   AÉREA   : {es_palindromo("   AÉREA   ")}")
print(f"7.- Ne    U q U é N: {es_palindromo(" Ne    U q U é N")}")
print(f"8.- Anita lava la tina: {es_palindromo(" Anita lava la tina")}")
print(f"9.- Yo HAGO y o g a HOY: {es_palindromo("Yo HAGO y o g a HOY")}")
print(f"10.- Yo HAGO y o g a HOY a la tarde: {es_palindromo("Yo HAGO y o g a HOY a la tarde")}")

print("\n¡Muchas gracias y hasta luego!\n")