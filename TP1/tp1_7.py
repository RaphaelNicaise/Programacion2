"""
Realizar un programa que solicite al usuario un número entero positivo, y luego en 
pantalla muestre solamente los números pares desde el 1 hasta el número 
ingresado. 
Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10 
"""

n = int(input("Ingrese un numero: "))

for i in range(2,n+1,2): # De donde, hasta donde, pasos
    print(i)