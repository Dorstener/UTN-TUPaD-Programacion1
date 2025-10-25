# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

inventario = {'Lapiceras': 1000, 'Cuadernos': 250, 'Carpetas': 50, 'Calculadoras': 20, 'Marcadors': 750, 'Lapices': 2000, 'Folios': 430}

menu = "\n Bienvenidos a nuestra Libreria. Elija una opción:  \n>>> 1 - Consulta de stock \n>>> 2 - Agregar Stock a un producto existente \n>>> 3 - Agregar nuevo producto al inventario >>> \n>>> 4 - Salir"

while True:
    print(menu)
    opcion = int(input("Elija una opción: "))

    match opcion:

        case 1:
            busqueda = input("Ingrese el nombre del producto del cual desea saber el stock: ")
            if busqueda in inventario:
                print(f"El producto {busqueda} tiene {inventario[busqueda]} stock en el inventario")

        case 2:
            agregar_producto_stock = input("Ingrese el nombre del producto al cual desea agregar stock: ")
            if agregar_producto_stock in inventario:
                agregar_stock = int(input("Ingrese la cantidad de stock que desea agregarle a este producto: "))
                inventario[agregar_producto_stock] = inventario[agregar_producto_stock] + agregar_stock
                print(f"El nuevo stock de {agregar_producto_stock} es {inventario[agregar_producto_stock]}")
            else:
                print("Ese producto no existe en nuestro inventario. Por favor, agregarlo")

        case 3:
            nuevo_producto = input("Ingrese el nombre del nuevo producto a agregar al Inventario: ")
            nuevo_producto_stock = int(input("Ingrese el stock del nuevo producto agregado al Inventario: "))
            inventario[nuevo_producto] = nuevo_producto_stock
            print(f"Con su última adición de productos, este es el estado actual del inventario: {inventario}")

        case 4:
            print("Gracias por su visita")
            break