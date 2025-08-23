# Ejercicio 6: Detector de años bisiestos
# Objetivo: Aplicar condiciones compuestas.
# Instrucciones:
#1. Pide un año al usuario.
#2. Si es divisible por 4 pero no por 100, o divisible por 400, imprime: "Se ingresó un año bisiesto".
# 3. En otro caso, imprime: "Se ingresó un año no bisiesto".

ano = int(input("Ingrese un año:  "))

if ((ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0)):
    print("Se ingresó un año bisiesto")
else:
    print("Se ingresó un año no bisiesto")



# Preguntas de reflexión:
# 1) ¿Por qué el año 1900 no es bisiesto?
# Poruqe es divisible por 100 pero no por 400

# 2) ¿Cómo validarías que el año sea positivo?
# Haría un condicional para ver si el numero ingresado es mayor o igual a uno, sino solicitaría ingresar nuevamente un numero