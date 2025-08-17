#Ejercicio 1

#Enunciado:  Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hello World")

#Ejercicio 2

#Enunciado: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Cual es tu nombre?")
print (f"Hola {nombre} !")


#Ejercicio 3

#Enunciado: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre = input("Cual es tu nombre?")
apellido = input ("Cual es tu apellido?")
edad = input("Que edad tenes?")
residencia = input ("Donde vivis?")
print(f"Soy {nombre} {apellido}, tengo {edad} anhos y vivo en {residencia}")

#Ejercicio 4

#Enunciado: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio de un circulo: "))
pi = 3.14
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"{area} es el area del circulo y {perimetro} es su perimetro")


#Ejercicio 5

#Enunciado: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 

seg = int(input("Ingrese una cantidad de segundos: "))
hrs = (seg * 1)/3600
print(f"Su cantidad de segundos traducidos a la unidad de horas es de {hrs}")

#Ejercicio 6

#Enunciado: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.  

numero = int(input("Ingrese un numero del 1 al 10: "))
x1 = numero * 1
x2 = numero * 2
x3 = numero * 3
x4 = numero * 4
x5 = numero * 5
x6 = numero * 6
x7 = numero * 7
x8 = numero * 8
x9 = numero * 9
x10 = numero * 10
print(f"Aqui tiene la tabla de multiplicar del numero ingresado. X1 es igual a {x1}, X2 es igual a {x2}, X3 es igual a {x3}, X4 es igual a {x4}, X5 es igual a {x5}, X6 es igual a {x6}, X7 es igual a {x7}, X8 es igual a {x8}, X9 es igual a {x9}, X10 es igual a {x10}, ")


#Ejercicio 7

#Enunciado: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))


suma= num1 + num2
div= num1 / num2
mult= num1 * num2
rest= num1 - num2


print(f"La suma de los dos numeros ingresados es de {suma}")
print(f"La division de los dos numeros ingresados es de {div}")
print(f"La multiplicacion de los dos numeros ingresados es de {mult}")
print(f"La resta de los dos numeros ingresados es de {rest}")


# Ejercicio 8 

# Enunciado: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:  

#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)

altura = float(input("Ingrese su altura expresada en metro: "))
kg = int(input("Ingrese su peso expresado en kg: "))
imc = kg/(altura ** 2)
print(f"Su indice de masa corporal es de {imc}")


#Ejercicio 9

#Enunciado: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠   + 32

temp = float(input("Ingrese la temperatura actual expresada en Celsius, para ser traducida a Fahrenheit: "))
fahren = (9/5 * temp) +32
print(f"La temperatura ingresa traducida a Fahrenheit es igual a {fahren}")


#Ejercicio 10

#Enunciado: Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))
promedio = (num1 + num2 + num3)/3
print(f"El promedio de los 3 numeros ingresados es {promedio}")

