"""
11. Escriba un programa que permita el ingreso de números enteros positivos para 
calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número 
negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej: 
“El promedio es ..... con un total de .... ingresos.” 
"""

ingresos = 0
suma = 0
n = 0
while n >= 0:
    n = int(input("Ingrese numeros para calcular su promedio (negativo para terminar) -> "))
    if n >= 0:
        suma += n
        ingresos += 1
print(ingresos)
promedio = suma/ingresos
print(f"El promedio es {promedio}")