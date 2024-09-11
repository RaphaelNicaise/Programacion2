"""
Escriba un programa que para un texto ingresado nos muestre cual es la palabra 
más larga dentro de ese texto y cuántas letras tiene. 
"""

texto = input("Ingrese un texto -> ")
palabras = texto.split(sep=" ")
print(palabras)

palabra_mas_larga = ''
for i in range(len(palabras)):
    if len(palabras[i]) > len(palabra_mas_larga):
        palabra_mas_larga = palabras[i]
        
print("La palabra mas larga es:",palabra_mas_larga)
     