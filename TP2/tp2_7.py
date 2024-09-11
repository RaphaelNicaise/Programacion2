"""
Un almacén guarda los códigos, los nombres de los productos y sus precios, 
respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer 
un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del 
archivo y buscar el precio de un artículo ingresado por teclado. Para probar el 
algoritmo crear un archivo “productos.txt” y cargarle datos al estilo: 
100;arroz;10 
102;fideos;5 
135;lentejas;8 
138;porotos;6 
140;sal gruesa;5 
201;aceite;20       (  etc...  ) 
"""

def leer_txt() -> list:
    with open("productos.txt", "r") as archivo:
        productos = list()
        lineas = archivo.readlines()
            
        for linea in lineas:
            id,nombre,precio = linea.strip().split(';')
            producto = dict(id=int(id),nombre=nombre,precio=int(precio))
            productos.append(producto)
            
        archivo.close()
    return productos

productos = leer_txt()

while True:
    try:
        producto_buscado = int(input("Buscar precio del id producto -> "))
        if producto_buscado in [producto['id'] for producto in productos]:
            break
        raise ValueError
    except ValueError:
        print("Tenes que ingresar un id valido")

id_encontrado = False
for producto in productos:
    if producto['id']==producto_buscado:
        id_encontrado = True
        print(f"El precio del producto id: {producto_buscado} es -> {producto['precio']}$")



        
            
    