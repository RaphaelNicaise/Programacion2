import random

"""
Escriba un programa que permita leer de un archivo distancias.txt (cada renglón 
tiene una distancia válida) las distancias recorridas por el vehículo de una empresa, 
luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y 
todas las distancias mayores al promedio. 
Ej del contenido del archivo: 
150 
120 
50 
34 
250 
Salida: “La distancia promedio de los viajes es ... y los viajes con distancia mayor 
son: ... , ... , .... , .... “ 
"""
distancias = []
def write_txt_random():
    with open("distancia.txt","w") as archivo:
        for _ in range(20):
            distancia = random.randint(1, 500)
            archivo.write(str(distancia)+"\n")

write_txt_random()

with open("distancia.txt","r") as archivo:
    while True:
        renglon = archivo.readline()
        if not renglon:
            break
        distancias.append(int(renglon))
    archivo.close()
    
print(distancias)

cantidad_viajes = len(distancias)

suma = 0
for viaje in distancias:
    suma += viaje
    
promedio = suma/cantidad_viajes

print(f"{suma}km hechos en {cantidad_viajes} viajes da un promedio de {promedio}km por viaje")

print("Distancias mayores al promedio:")
#                  que guarda por iteracionvariable, recorrido, condicion
distancias_mayores = [viaje for viaje in distancias if viaje > promedio]
print(distancias_mayores)