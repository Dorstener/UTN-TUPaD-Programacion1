# Actividad 6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

print("_"*40, "\n")
print(f"Actividad 6\n")
print("¡Hola!\n")

def suma_digitos(n):
    if n<10:
        return n
    else:
        return suma_digitos(n//10) + n%10

print(f"1234 = 1 + 2 + 3 + 4 = {suma_digitos(1234)}")
print(f"9 = {suma_digitos(9)}")
print(f"305 = 3 + 0 + 5 = {suma_digitos(305)}")   

print("\n¡Muchas gracias y hasta luego!\n")