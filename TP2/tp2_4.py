"""
Escriba un programa que permita ingresar un número, se debe validar que 
realmente se haya ingresado un número, y crear una lista para almacenar por 
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que 
contiene el dígito mayor. 
"""

def ingresar_numero()->int:
    while True:
        try:
            num = int(input("Ingrese numero -> "))
            break
        except ValueError:
            print("Error al ingresar numero")
    return num

def indice_digito_mayor(numero:int)->int:
    digito_mayor = 0
    lista_numeros = [int(digito) for digito in str(numero)]
    for i in range(0,len(lista_numeros)):
        if digito_mayor < lista_numeros[i]:
            digito_mayor = lista_numeros[i]
    
    return lista_numeros.index(digito_mayor)
    

numero = ingresar_numero()       
print(f" El indice del digito mayor del numero {numero} es {indice_digito_mayor(numero)}")

