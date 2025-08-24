

# Solicitamos frase al usuario
frase = str(input("Ingrese su frase o palabra favorita: "))

# Utilizamos .lower para llevar a minuscula una posible mayuscula utilizada en la palabra/frase
# Utilizamos .endswith para chequear en que letra termina la palabra/frase e insertamos los valores que queremos chequear, en este caso vocales

if frase.lower().endswith(("a", "e", "i", "o", "u")):
    print(f"{frase}!")
else:
    print(frase)