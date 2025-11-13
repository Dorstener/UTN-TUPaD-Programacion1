# Actividad 4. Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

print("_"*40, "\n")
print(f"Actividad 4\n")
print("¡Hola!\n")

# Fución recursiva para convertir un número entero positivo decimal en binario
def convertir_a_binario(decimal):
    if decimal<0:
        return "Disculpe, pero sólo funciona con numeros enteros positivos en base 10"   
    elif decimal==0:
        return "0"
    elif decimal==1:
        return "1"
    else:
       return f"{convertir_a_binario(decimal//2)}{decimal%2}"
    
print(f"El número decimal 13 en binario es: {convertir_a_binario(13)}")
print(f"El número decimal 0 en binario es: {convertir_a_binario(0)}")
print(f"El número decimal 1 en binario es: {convertir_a_binario(1)}")
print(f"El número decimal -13 en binario es: {convertir_a_binario(-13)}")

print("\n¡Muchas gracias y hasta luego!\n")
