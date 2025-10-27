# Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt","w") as archivo:
    archivo.write("Pelota,80,50\n")
    archivo.write("Camiseta de Futbol,120,250\n")
    archivo.write("Guantes de Arquero,10,30\n")