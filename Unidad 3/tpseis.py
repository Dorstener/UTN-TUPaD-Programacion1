import random
import statistics

numeros_aleatorios = [random.randint(1,100) for i in range (50)]

mean = (statistics.mean(numeros_aleatorios))
median = (statistics.median(numeros_aleatorios))
mode = (statistics.mode(numeros_aleatorios))

print(mean)
print(median)
print(mode)

if (mean > median > mode):
    print("Hay un sesgo positivo a la derecha")
elif (mean < median < mode):
    print("Hay un sesgo negativo a la izquierda")
elif (mean == median == mode):
    print("No hay sesgo (distribución simétrica)")
else:
    print("La relación no encaja en los tres casos clásicos")