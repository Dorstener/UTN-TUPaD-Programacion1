# Actividad 8.  Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#      Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0   

print("_"*40, "\n")
print(f"Actividad 8\n")
print("¡Hola!\n")

def contar_digito(numero, digito):
    numero=abs(numero)
    if digito<0 or digito>10:
        return "Disculpe, hay un error: El dígito debe estar entre 0 y 9"
    if numero<10:
        return 1 if numero==digito else 0
    else:
        return (1 if numero%10==digito else 0) + contar_digito(numero//10, digito)

print("Ejemplos de contar dígitos en un número:\n")
print(f"1. En el número 12233421, el dígito 2 aparece: {contar_digito(12233421, 2)} veces") 
print(f"2. En el número 5555, el dígito 5 aparece:  {contar_digito(5555, 5)} veces")
print(f"2. En el número 123456, el dígito 7 aparece:  {contar_digito(123456, 7)} veces") 
print(f"3. En el número 0, el dígito 0 aparece:  {contar_digito(0, 0)} veces")
print(f"4. En el número -132334353, el dígito 3 aparece:  {contar_digito(-132334353, 3)} veces")
print(f"3. En el número 12345, el dígito -3 aparece:  {contar_digito(12345, -3)} veces")
print(f"3. En el número 12345, el dígito 12 aparece:  {contar_digito(12345, 12)} veces")

print("\n¡Muchas gracias y hasta luego!\n")