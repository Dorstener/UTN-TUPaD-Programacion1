# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista_productos = []


for x in range(5):
    lista_productos.append(input("Ingrese un producto: "))



print(lista_productos)
lista_ordenada = sorted(lista_productos)
print(lista_ordenada)

lista_ordenada.remove(input("Que elemento desea borrar: "))
print(lista_ordenada)


# Otra opción de resolución del ejercicio, validando el producto a borrar y actualizando la lista con un nuevo producto

# borrar = input("Que elemento desea borrar: ")
#if (borrar == lista_productos[0]):
#    lista_productos[0] = input("Ingrese el nuevo producto a su lista: ")
#elif (borrar == lista_productos[1]):
#    lista_productos[1] = input("Ingrese el nuevo producto a su lista: ")
#elif (borrar == lista_productos[2]):
#    lista_productos[2] = input("Ingrese el nuevo producto a su lista: ")
#elif (borrar == lista_productos[3]):
#    lista_productos[3] = input("Ingrese el nuevo producto a su lista: ")
#elif (borrar == lista_productos[4]):
#    lista_productos[4] = input("Ingrese el nuevo producto a su lista: ")

#lista_ordenada = sorted(lista_productos)
#print(lista_ordenada)
