"""
El mismo almacén del punto anterior almacena los datos del stock de productos en 
el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de 
producto; stock mínimo; stock real”. Escriba un programa, que a partir de 
información contenida en los archivos, genere otro archivo de texto, Compras.txt, 
conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo. 
Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y 
cargarle datos utilizando los códigos de los productos del archivo anterior. Ej: 
100;50;60 
102;50;20 
135;20;15 
138;20;20 
140;10;8 
201;20;30       (  etc...  ) 
"""

def leer_txt_stocks() -> list:
    with open("stock.txt", "r") as archivo:
        productos = list()
        lineas = archivo.readlines()
            
        for linea in lineas:
            id,stock_minimo,stock_real = linea.strip().split(';')
            producto = dict(id=int(id),stock_minimo=int(stock_minimo),stock_real=int(stock_real))
            productos.append(producto)
            
        archivo.close()
    return productos

stock_productos = leer_txt_stocks()
for stock_producto in stock_productos:
    print(stock_producto)

def leer_txt_productos()->list:
    with open("productos.txt", "r") as archivo:
        productos = list()
        lineas = archivo.readlines()
            
        for linea in lineas:
            id,nombre,precio = linea.strip().split(';')
            producto = dict(id=int(id),nombre=nombre,precio=int(precio))
            productos.append(producto)
            
        archivo.close()
    return productos

productos = leer_txt_productos()

def obtener_producto_por_id(id:int)->str:
    for producto in productos:
        if producto['id']==id: return producto['nombre']

for producto in productos:
    print(producto)

productos_a_guardar = []    
for producto in stock_productos:
    id = producto['id'] 
    if producto['stock_minimo'] > producto['stock_real']:
        productos_a_guardar.append(obtener_producto_por_id(id))

def escribir_compras_txt(productos_a_guardar:list):                                
    with open("compras.txt","w") as archivo:
        for producto in productos_a_guardar:
            archivo.write(producto+"\n")

escribir_compras_txt(productos_a_guardar)
