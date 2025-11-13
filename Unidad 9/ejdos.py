# Actividad 2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

print("_"*40, "\n")
print(f"Actividad 2\n")
print("¡Hola!\n")

# Función para calcular el valor de la serie de Fibonacci en la posición indicada
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
    
# Pedir al usuario un número entre 0 y 35, porque más de 35 tarda mucho en aparecer el resultado
print(f"Ingresa un número entero entre 1 y 35 para ver la serie de Fibonacci hasta esa posición: ", end="")   
def validar_entre_1y35():
    valido=False
    while not valido:
        num=input().strip()
        try:
            numero=int(num)
            if 0<numero<36:   
                return numero
            else:
                print(f"Disculpe, pero {numero} no es un número entero entre 1 y 35, intente nuevamente: ", end="")
        except ValueError:
            print("Disculpe, pero no ha ingresado un número entero entre 1 y 35, intente nuevamente: ", end="")

numero=validar_entre_1y35()

#  Mostrar la serie completa hasta la posición dada
print(f"\nLa serie de Fibonacci hasta la posición {numero} es: ", end="")
for i in range(numero):   
    print(f"{fibonacci(i)} ", end="") 

print("\n¡Muchas gracias y hasta luego!\n")
