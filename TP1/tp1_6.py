"""
Realizar un programa que solicite al usuario un número entero positivo, y luego en 
pantalla muestre la secuencia de números desde el 1 hasta el número ingresado. 
Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10 
"""

try: 
    n = int(input("Ingresa un numero entero positivo: "))
    for i in range(n):
        print(i+1)
except ValueError as e:
    print("Pone un numero flaco")
