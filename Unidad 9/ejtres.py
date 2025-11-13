# Actividad 3. Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

print("_"*40, "\n")
print(f"Actividad 4\n")
print("¡Hola!\n")

# Definir la función potencia, donde bas=base y exp=exponente de la potencia
# Esta función sólo trabaja con exponentes enteros
def potencia(bas,exp):
    if exp<0 and bas!=0:
        return 1/potencia(bas,-exp)
    elif bas==0:
        if exp==0:
            return "Indeterminado"
        elif exp<0:
            return "No se puede dividir entre 0"
        else:
            return 0
    elif bas==1 or exp==0:
        return 1
    else:
       return bas*potencia(bas,exp-1)

            

print("\nProbando la función de potencia usando recursividad:")    
print(f"2 elevado a la 6: {potencia(2,6)}")
print(f"0 elevado a la 0: {potencia(0,0)}")
print(f"0 elevado a la 5: {potencia(0,5)}")
print(f"1 elevado a la 0: {potencia(1,0)}")
print(f"1 elevado a la 45: {potencia(1,45)}")
print(f"-1 elevado a la 45: {potencia(-1,45)}")
print(f"-3 elevado a la 4: {potencia(-3,4)}")
print(f"-3 elevado a la 3: {potencia(-3,3)}")
print(f"2 elevado a la -1: {potencia(2,-1)}")
print(f"2 elevado a la -3: {potencia(2,-3)}")
print(f"1 elevado a la -1: {potencia(1,-3)}")
print(f"0 elevado a la -4: {potencia(0,-4)}")

print("\n¡Muchas gracias y hasta luego!\n")
