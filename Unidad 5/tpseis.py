# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

lista = [4,7,3,9,12,1,8]

lista_uno = []
lista_dos = []
la_gran_lista = []

lista_uno.append(lista[6])
lista.remove(8)

la_gran_lista = lista_uno + lista

print(la_gran_lista)

