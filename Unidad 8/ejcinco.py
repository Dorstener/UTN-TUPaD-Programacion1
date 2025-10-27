# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

lista_productos = []

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

buscar_producto = input("\nQue producto desea buscar: ")

encontrado = False
for producto in lista_productos:
        if producto['Nombre'] == buscar_producto:
            print(f"\nProducto Encontrado: \nNombre: {producto['Nombre']}, Precio: ${producto['Precio']}, Cantidad: {producto['Cantidad']}")
            encontrado = True
            break
if not encontrado:
    print(f"\nEl producto que busca no se encuentra en nuestro catalogo")