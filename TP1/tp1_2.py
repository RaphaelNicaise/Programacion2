"""
Implemente un programa que a partir del ancho, alto y largo de una habitación
rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo
que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una
puerta de 0,80 de ancho por 2 mts de alto. 
"""

ancho = float(input("Ancho de la habitacion: "))
alto = float(input("Alto de la habitacion: "))
largo = float(input("Largo de la habitacion: "))

area_a_pintar = (ancho*alto*2) + (largo*alto*2) - 0.80*2
un_litro = 10 # 10 metros
litros_pintura = area_a_pintar/un_litro
print(f"Van a ser necesarios {litros_pintura} litros de pintura")