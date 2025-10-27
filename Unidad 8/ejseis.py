lista_productos = []

# Leer archivo y organizar la lista

with open("productos.txt","r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue
        
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "Nombre": nombre,
            "Precio": int(precio),
            "Cantidad": int(cantidad),
        }
        lista_productos.append(producto)

# Agregar un nuevo producto a la lista (NO al archivo)

with open("productos.txt","a") as archivo:
    print("\n ---->>>  Agregar un nuevo Producto  <<<-----")
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    archivo.write(f"{nombre},{precio},{cantidad}\n")
    print(f"\n El producto: {nombre} fue agregado correctamente")

# Buscar productos

buscar_producto = input("\nQue producto desea buscar: ")

encontrado = False
for producto in lista_productos:
        if producto['Nombre'] == buscar_producto:
            print(f"\nProducto Encontrado: \nNombre: {producto['Nombre']}, Precio: ${producto['Precio']}, Cantidad: {producto['Cantidad']}")
            encontrado = True
            break
if not encontrado:
    print(f"\nEl producto que busca no se encuentra en nuestro catalogo")


# Guardar la lista Actualizada al archivo

with open("productos.txt","w") as archivo:
    for producto in lista_productos:
        linea = f"{producto['Nombre']},{producto['Precio']},{producto['Cantidad']}\n"
        archivo.write(linea)

print("Archivo 'productos.txt'actualizado correctamente")
print(lista_productos)