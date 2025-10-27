# Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

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
        
    for producto in lista_productos:
        print(f"Producto: {producto['Nombre']} | Precio: ${producto['Precio']} | Cantidad: {producto['Cantidad']}")