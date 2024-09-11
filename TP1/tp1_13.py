"""Se desea realizar una aplicación que solicite al usuario un caracter y un número 
natural N, y que la aplicación muestre en pantalla dicho carácter repetido N veces 
consecutivas. 
Ej:  Ingrese un caracter: + 
 Ingrese la cantidad de repeticiones: 15 
 +++++++++++++++ 
"""

char = input("Ingrese un caracter -> ")
while True:
    try:
        n = int(input("Ingresa un numero -> "))
        break
    except ValueError:
        print("Tenes que ingresar un numero, no un caracter /:")

print(n*char)