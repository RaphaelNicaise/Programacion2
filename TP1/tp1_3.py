"""
Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura.
"""
ancho = float(input("Ancho de la habitacion: "))
alto = float(input("Alto de la habitacion: "))
largo = float(input("Largo de la habitacion: "))
manos = int(input("Manos de pintura: "))
area_a_pintar = ((ancho*alto*2) + (largo*alto*2) - 0.80*2)*manos

un_litro = 10 # 10 metros
litros_pintura = area_a_pintar/un_litro
print(f"Van a ser necesarios {litros_pintura} litros de pintura")