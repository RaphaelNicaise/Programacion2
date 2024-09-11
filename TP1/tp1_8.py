"""
8. Desarrollar un programa que permita al usuario indicar cuantos valores quiere 
ingresar, luego que permita la carga de los valores por teclado y nos muestre 
posteriormente la suma de los valores ingresados y su promedio. 
"""

suma = 0
promedio = 0

numeros = int(input("Cuantos numeros queres ingresar? -> "))

for i in range(numeros): # de 0 al numero
    suma += int(input(f"Ingrese n°{i+1}: "))
    
promedio = suma/numeros
print(f"Suma: {suma} Promedio: {promedio}") 