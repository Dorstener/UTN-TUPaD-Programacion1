# Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt","r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

with open("productos.txt","a") as archivo:
    print("\n ---->>>  Agregar un nuevo Producto  <<<-----")
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    archivo.write(f"{nombre},{precio},{cantidad}\n")
    print(f"\n El producto: {nombre} fue agregado correctamente")

