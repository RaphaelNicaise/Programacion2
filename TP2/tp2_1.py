"""
Escribir un procedimiento “reverso” que permita ingresar como parámetro una 
cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego 
un programa que determine si una cadena de caracteres es un palíndromo (un 
palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”). 
Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas, 
utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es 
distinto a radaR
"""

def reverso(cadena:str)->str:
    invertida = ""
    for i in range(len(cadena)):
        invertida += cadena[len(cadena)-1-i]
    return invertida.lower()

def esPalindromo(cadena:str)->bool:
    largo_cadena = len(cadena)
    palindromo = True

    for i in range(largo_cadena):
        if cadena[i] != cadena[largo_cadena-i-1]:
            return False
    return palindromo

def main():
    palabra_invertida = reverso(input("Ingrese una cadena -> "))
    print(palabra_invertida)
    if esPalindromo(palabra_invertida):
        print("La cadena es palindromo")
    else:
        print("La cadena no es palindromo")

if __name__:
    main()