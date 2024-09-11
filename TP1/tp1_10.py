"""
10. Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un 
rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje 
en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más 
largo, con el fin de evitar problemas de visualización en la consola. Verificar en los 
datos de entrada que se cumpla este requisito. 
"""
base = 0
altura = 0

while base > 40 or base <= 0: 
    base = int(input("Ingresar base del rectangulo: "))
while altura > 40 or altura <= 0:    
    altura = int(input("Ingresar altura del rectangulo: "))

for i in range(altura):
    print("*"*base)