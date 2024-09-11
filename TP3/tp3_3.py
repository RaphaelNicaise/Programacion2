"""
Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas 
las líneas del archivo, utilizando list comprehensions.
"""

def leer_txt()->list:
    with open("datos.txt","r") as archivo:
        lineas = archivo.readlines()
        lista_lineas = [int(linea.strip()) for linea in lineas if linea]
        archivo.close()
        return lista_lineas
    
print(leer_txt())