"""
Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de 
vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste 
introduzca la palabra “salir”.
"""

def contar_vocales(string:str)->int:
    string = string.lower()
    vocales = [letra for letra in string if letra in {'a','e','i','o','u'}]
    cantidad_vocales = len(vocales)
    return cantidad_vocales
    
while True:
    palabra = input("Ingresa palabra para contar sus vocales -> ").lower()
    if palabra == 'salir':
        break 
    if palabra:
        cant_vocales = contar_vocales(palabra)
        if cant_vocales > 0: print(f"Hay {cant_vocales} vocales en la palabra {palabra}") 
        else: print(f"No hay vocales en la palabra {palabra}")

     