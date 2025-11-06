import csv
import os

# Variable creada para guardar el nombre del archivo CSV a utilizar en todo el ejercicio
Nombre_Archivo = "catalogo_de_libros.csv"

############# DEFINICION DE FUNCIONES ############

# Funcion 0: Mostrar el menu

def mostrar_menu():

    print("\n")
    print("===== Biblioteca Escolar - Catalogo de Libros =====\n")
    print("Opción 1 >>> Mostrar todo el catalogo")
    print("Opción 2 >>> Ingrese un título al catalogo")
    print("Opción 3 >>> Ingrese múltiples título al catalogo")
    print("Opción 4 >>> Mostrar titulos con stock agotados")
    print("Opción 5 >>> Consulte stock de un título existente del catalogo")
    print("Opción 6 >>> Ingrese ejemplares a un título existente del catalogo")
    print("Opción 7 >>> Actualizar stock de un título del catalogo (prestamo/devolucion)")
    print("Opción 8 >>> Salir")
    print("\n")
    print("===== xxxxx =====\n")

# Funcion 1.0: Funcion para mostrar Catalogo de titulos de la Biblioteca Escolar

def catalogo():
    print("=====>>>>> Catalogo de la Biblioteca <<<<<=====\n")
    catalogo_libros = obtener_catalogo()
    
    for libro in catalogo_libros:
        print(f"Título: '{libro['Titulo']}' - Ejemplares: {libro['Ejemplares']}" )

# Funcion 1.1: Funcion para crear y para retrieve el catalogo de Libros

def obtener_catalogo():
    
    catalogo_libros = []
    
# Si el archivo no existe, entonces crea el encabezado

    if not os.path.exists(Nombre_Archivo):
        with open(Nombre_Archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
            escritor.writeheader()
        return catalogo_libros

# Si el archivo ya existe, entonces se leen los datos

    with open(Nombre_Archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            catalogo_libros.append({"Titulo": str(fila["Titulo"]), "Ejemplares": int(fila["Ejemplares"])})
        return catalogo_libros

# Funcion 2.0: Funcion para ingresar un titulo al Catalogo

def ingresar_titulo():
    catalogo_libros = obtener_catalogo()
    print("=====>>>>> Ingresar titulo al Catalogo de la Biblioteca <<<<<=====\n")

# Le pedimos al usuario el ingreso de un titulo, y lo validamos. Usé .strip()) y .title() para normalizarlo
    
    titulo = str(input("Ingrese nombre del Título a ingresar al catalogo: ")).strip().title()
    titulo_valido = validacion_nuevo_titulo(catalogo_libros, titulo)

    if titulo_valido is None:
        print("Vuelva a intentarlo\n")
        return

# Le pedimos al usuario la cantidad y la validamos. Usé .strip()) y .title() para normalizar el ingreso

    ejemplares = str(input(f"Ingrese la cantidad de ejemplares para el titulo {titulo}: ").strip())
    ejemplares_valido = validacion_nuevos_ejemplares(ejemplares)

    if ejemplares_valido is None:
        print("Vuelva a intentarlo\n")
        return
    
# Guardamos el nuevo ingreso en el archivo CSV

    with open(Nombre_Archivo,"a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["Titulo","Cantidad"])
        escritor.writerow({
            "Titulo": titulo,
            "Ejemplares": ejemplares_valido
        })
        print(f"\nUsted ha ingresado el siguiente titulo: '{titulo}' al Catalogo de la Biblioteca Escolar. A ese título, le ha asignado {ejemplares_valido} ejemplares\n")

    
# Función   : Función para ingresar múltiples titulos al Catalogo de la Biblioteca

def ingresar_multiples_titulos():
    catalogo_libros = obtener_catalogo()
    print("=====>>>>> Ingresar múltiples titulos al Catalogo de la Biblioteca <<<<<=====\n")

# Le pedimos al usuario que nos diga cuantos libros quiere ingresar. Validamos su input

    while True: 
        cant_libros_ingresar = input("Cuántos libros desea ingresar al Catalogo de la Biblioteca Escolar?: ")
        cant_libros_ingresar_valido = validacion_nuevos_ejemplares(cant_libros_ingresar)

        if cant_libros_ingresar_valido is None:
            print("Vuelva a intentarlo\n")
            continue

# Usamos ciclo for combinando con la cantidad de titulos que el usuario quiere ingresar, para capturar de esa forma todos los titulos que quiere ingresar el usuario y validarlos.

        for x in range(1, cant_libros_ingresar_valido + 1):
            
            while True:    
                titulo = str(input(f"Ingrese nombre del Título {x} a ingresar al catalogo: ")).strip().title()
                titulo_valido = validacion_nuevo_titulo(catalogo_libros, titulo)

                if titulo_valido is None:
                    print("Vuelva a intentarlo\n")
                    continue
                break

# Lo mismo, seguimos dentro del ciclo for y le pedimos al usuario que ingrese la cantidad de ejemplares para cada titulo a ingresar.

            while True:

                ejemplares = str(input(f"Ingrese la cantidad de ejemplares para el titulo {titulo}: ").strip())
                ejemplares_valido = validacion_nuevos_ejemplares(ejemplares)

                if ejemplares_valido is None:
                    print("Vuelva a intentarlo\n")
                    continue
                break

# vamos guardando cada ingreso en el CSV

            with open(Nombre_Archivo,"a", newline="", encoding="utf-8") as archivo:
                    escritor = csv.DictWriter(archivo, fieldnames=["Titulo","Cantidad"])
                    escritor.writerow({
                    "Titulo": titulo,
                    "Ejemplares": ejemplares_valido
                })

            catalogo_libros.append({"Titulo": titulo, "Ejemplares": ejemplares_valido})
            print(f"\nUsted ha ingresado el siguiente titulo: '{titulo}' al Catalogo de la Biblioteca Escolar. A ese título, le ha asignado {ejemplares_valido} ejemplares\n")
        return
    
# Función   : Función para mostrar los titulos con el stock agotado en el Catalogo de la Biblioteca

def titulos_stock_agotado():
    catalogo_libros = obtener_catalogo()
    print("=====>>>>> Títulos con stock agotado en el Catalogo de la Biblioteca <<<<<=====\n")

    sin_stock = False

# usamos un ciclo for para recorrer todo el listado de libros y usamos un if, para identificar que titulo tiene 0 ejemplares. Una vez identificado, lo printeamos

    for libro in catalogo_libros:
        if int(libro["Ejemplares"]) == 0:
            print(f"{libro['Titulo']} - {libro['Ejemplares']}") 
            sin_stock = True
        
    if not sin_stock:
        print("No hay titulos con stock agotado\n")

# Función   : Función para consultar stock de un titulo existente en el Catalogo de la Biblioteca

def consulta_stock():
    catalogo_libros = obtener_catalogo()
    print("=====>>>>> Consulta de stock de un título existente en el Catalogo de la Biblioteca <<<<<=====\n")

    titulo = input("Ingrese el titulo del libro para el cual desea consultar su stock: ").strip().title()
    
    if not titulo:
        print("Error: El titulo no puede estar vacio\n")
        return None
    
    titulo_encontrado = False

# usamos un ciclo for para recorrer todo el catalogo de libros, ver si el titulo se encuentra en el catalogo, y si esta, entonces lo printeamos

    for libro in catalogo_libros:
        if libro["Titulo"] == titulo:
            print(f"\nEl titulo '{libro['Titulo']}' tiene {libro['Ejemplares']} ejemplares disponibles en nuestro Catalogo")
            titulo_encontrado = True
            break
        
    if not titulo_encontrado:
        print("\nEl titulo que está buscando no existe en nuestro Catalogo")
        print("Puede consultar el catalogo completo seleccionando la opción 1 del menu principal")

# Función   : Función para ingresar stock a un titulo existente en el Catalogo de la Biblioteca

def ingresar_ejemplares():
    catalogo_libros = obtener_catalogo()
    print("=====>>>>> Ingreso de ejemplares a un título existente Catalogo de la Biblioteca <<<<<=====\n")

    titulo = input("Ingrese el titulo al que desea agregar ejemplares: ").strip().title()
    
    if not titulo:
        print("Error: el titulo no puede estar vacio\n")
        return
    
    encontrado = False

# ciclo for para recorrer el catalogo de libros. Si el libro esta, le preguntamos al usuario cuantos ejempalres le desea agregar a ese libro y guardamos la entrada

    for libro in catalogo_libros:
        if libro["Titulo"] == titulo:
            encontrado = True
            print(f"\nTitulo encontrado: '{libro['Titulo']}")
            print(f"Ejemplares actuales: {libro['Ejemplares']}\n")

            nuevos_ejemplares = input("Ingrese la cantidad de ejemplares a agregar: ").strip()
            nuevos_ejemplares_validados = validacion_nuevos_ejemplares(nuevos_ejemplares)

            if nuevos_ejemplares_validados is None:
                continue

            libro["Ejemplares"] = int(libro["Ejemplares"]) + nuevos_ejemplares_validados
            print(f"\nActualización existosa. Ahora el titulo '{libro['Titulo']}' tiene {libro['Ejemplares']} ejemplares")
    
            with open(Nombre_Archivo, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
                escritor.writeheader()
                for l in catalogo_libros:
                    escritor.writerow({"Titulo": l["Titulo"], "Ejemplares": l["Ejemplares"]})
            
            return
    
    if not encontrado:
        print(f"El titulo '{titulo}' no se encuentra en el catalogo/\n")
        print("Puede consultar el catálogo completo con la opción 1 del menú principal.\n")

# Función   : Función para actualizar el stock de un titulo del Catalogo de la Biblioteca

def actualizar_stock():
    catalogo_libros = obtener_catalogo()
    print("=====>>>> Actualización de stock de un título del Catalogo de la Biblioteca (prestamo/devolucion) <<<<<=====\n")

# Primero le mostramos al usuario las dos opciones, devolver, o prestamo
    print("Seleccione el tipo de operacion")
    print("1 - Préstamo de ejemplares")
    print("2 - Devolución de ejemplares")

    operacion = input("Ingrese el número de la operacion deseada: ").strip()

# validamos su input
    if operacion not in ["1","2"]:
        print("Opcion invalida. Debe ingresar 1 (prestamo) o 2 (devolucion).\n")
        return
    
    titulo = input("Ingrese el titulo del libro: ").strip().title()
    if not titulo:
        print("Error: el titulo no puede estar vacio.\n")
        return
    
    encontrado = False


    for libro in catalogo_libros:
        if libro["Titulo"] == titulo:
            encontrado = True
            print(f"\nTitulo encontrado: '{libro['Titulo']}'")
            print(f"\nEjemplares actuales: '{libro['Ejemplares']}'")

            cantidad = input("Ingrese la cantidad de ejemplares ").strip()
            cantidad_valida = validacion_nuevos_ejemplares(cantidad)

            if cantidad_valida is None or cantidad_valida <= 0:
                print("Error: debe ingresar un número válido mayor que cero.\n")
                return

#utillizamos un match, para adaptarlo a cada caso (prestamo/devolucion)

            match operacion:
                case "1": 
                    if libro["Ejemplares"] < cantidad_valida:
                        print("Error: no hay suficientes ejemplares disponibles para prestar.\n")
                        return
                    libro["Ejemplares"] = libro["Ejemplares"] - cantidad_valida
                    print(f"\n Se registró el prestamo de {cantidad_valida} ejemplar(es)")
                
                case "2":
                    libro["Ejemplares"] = libro["Ejemplares"] + cantidad_valida
                    print(f"Se registró la devolución de {cantidad_valida} ejemplar(es).")
                
            print(f"Stock actualizado: ahora '{libro['Titulo']}' tiene {libro['Ejemplares']} ejemplares")

            with open(Nombre_Archivo, "w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=["Titulo", "Cantidad"])
                escritor.writeheader()
                for l in catalogo_libros:
                    escritor.writerow({"Titulo": l["Titulo"], "Ejemplares":l["Ejemplares"]})
            
            return
        
    if not encontrado:
        print(f"El titulo '{titulo}' no se encuentra en el catalogo.\n  ")
        print("Puede consultar el catalogo completo con la opción 1 del menu principal.\n")

# Función   : Función para salir del menu del Catalogo de la Biblioteca

def salir():
    print("=====>>>>> Gracias por utilizar nuestro sistema y Biblioteca Escolar <<<<<=====")
    
############# FUNCIONES DE VALIDACION #################

# Validación 1: Funcion para validar la opcion ingresada por el usuario.
def validacion_opcion_menu():
            while True:
                opcion = input("Ingrese el número de la opción deseada: \n").strip() # use strip() para remover cualquier espacio extra agregado por el usuario
        
                # 1era validación, si el usuario no ingresa un digito, le informamos del error        
                if not opcion.isdigit():
                    print("Error: Por favor ingrese la opción deseada en número del 1 al 8\n")
                    continue
                else:
                    opcion = int(opcion)

                # 2da validación, verificamos que el numero de opcion ingresado esté dentro del rango 
                if 1 <= opcion <= 8:
                    return opcion
                else:
                    print("Error: Opción fuera de rango. Ingrese un número del 1 al 8\n")
                    continue

# Validacion 2: Funcion para validar un nuevo titulo ingresado por el usuario

def validacion_nuevo_titulo(catalogo_libros, titulo):

        if not titulo: 
                print("\nError: El titulo no puede estar vacio\n")
                return None

        for libro in catalogo_libros:
            if titulo == libro["Titulo"]:
                print(f"\nEl titulo '{titulo}' ya se encuentra en nuestro catalogo\n")
                return None
        
        return True

# Validacion 3: Funcion para validar una cantidad de ejemplares ingresada por el usuario

def validacion_nuevos_ejemplares(ejemplares):

    if not ejemplares.isdigit(): 
        print("Ingrese un número valido por favor\n")
        return None
    else:
        ejemplares = int(ejemplares)
        return ejemplares


################################################
############# PROGRAMA PRINNCIPAL ##############
################################################

while True: 
    mostrar_menu()
    opcion = validacion_opcion_menu()
    match opcion:

        case 1:
            catalogo()
        case 2:
            ingresar_titulo()
        case 3:
            ingresar_multiples_titulos()
        case 4:
            titulos_stock_agotado()
        case 5:
            consulta_stock()
        case 6:
            ingresar_ejemplares()
        case 7:
            actualizar_stock()
        case 8:
            salir()
            break