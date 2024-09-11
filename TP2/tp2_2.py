"""
Escriba una función llamada EsBisiesto que permita ingresar un número de año y 
devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año 
es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre 
400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por 
pantalla si la fecha es válida o no.
"""

def esBisiesto(anio:int)->bool:
    if anio % 4 == 0 and ((anio % 100 != 0) or (anio % 400 == 0 )):
        return True
    else:
        return False


try:  
        anio = int(input("Ingrese anio: "))
        if anio < 0:
            raise ValueError
        mes = int(input("Ingrese mes: "))
        if mes > 12 or mes < 1:
            raise ValueError
        dia = int(input("Ingrese dia: "))
        if dia > 31 or dia < 1:
            raise ValueError
        if esBisiesto(anio) and mes == 2 and dia==29:
            fecha_valida = True
        fecha_valida = True
except ValueError:
        print("Error al ingresar valor")
        fecha_valida = False
        
print(f"La fecha es valida? -> {fecha_valida}")