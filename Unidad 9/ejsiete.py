# Actividad 7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
 
#       Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

print("_"*40, "\n")
print(f"Actividad 7\n")
print("¡Hola!\n")

def contar_bloques(n):
    if n==0:
        return 0
    elif n<0:
        return "Disculpe, hay un error, no puede haber una cantidad de bloques negativa"
    else:
        return n + contar_bloques(n-1)
        

print("Ejemplos de contar bloques:\n")
print(f"1. si hay 1 bloque: {contar_bloques(1)}") 
print(f"2. si hay 4 bloques: 4 + 3 + 2 + 1 = {contar_bloques(4)}")
print(f"3. si hay 7 bloques: 7 + 6 + 5 + 4 + 3 + 2 + 1 = {contar_bloques(7)}") 
print(f"4. si hay 0 bloques: {contar_bloques(0)}")
print(f"5. si hay -3 bloque: {contar_bloques(-3)}")

print("\n¡Muchas gracias y hasta luego!\n")