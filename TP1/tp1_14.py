"""
Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad 
total de vocales que aparecen y lo muestre por pantalla. 
"""

vocales = ['a','e','i','o','u']

texto = input("Ingrese una palabra/texto: ")

cant_vocales = 0

for i in texto:
    if i in vocales:
        cant_vocales += 1


print("Cantidad de vocales: ")    
    