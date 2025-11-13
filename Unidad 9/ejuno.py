#-------------------------------------------------------------------------
# Actividad 1.Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

print("_"*40, "\n")
print(f"Actividad 1\n")
print("¡Hola!\n")

# Función recursiva para calcular el factorial de un número.
def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
    
# Función para validar que el usuario ingrese un número entero positivo menor que 999, se verificó que hasta
# ahí se puede usar la función recursiva    
def validar_entero_positivo_1a998():
    valido=False
    while not valido:
        num=input().strip()
        try:
            numero=int(num)
            if 0<numero<999:   # 0 no es un número entero positivo
                return numero
            else:
                print(f"Disculpe, pero {numero} no es un número entero entre 1 y 998, intente nuevamente: ", end="")
        except ValueError:
            print("Disculpe, pero no ha ingresado un número entero entre 1 y 998, intente nuevamente: ", end="")

# Calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario
print("Ingrese un número entero entre 1 y 998 para calcular el factorial desde 1 hasta ese número: ", end="")
numero=validar_entero_positivo_1a998()
for i in range(1,numero+1):
    print(f"El factorial de {i} es: {factorial(i)}")

print("\n¡Muchas gracias y hasta luego!\n")