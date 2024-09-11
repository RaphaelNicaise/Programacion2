"""
Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el 
mayor de los 3 y mostrar un mensaje por pantalla. 
"""

num1 = int(input("Ingresa numero 1: "))
num2 = int(input("Ingresa numero 2: "))
num3 = int(input("Ingresa numero 3: "))

if num1 == num2 == num3:
    print("Los numeros son iguales")
else:
    if num1 >= num2 and num1 >= num3:
        print(f"El numero mayor es el num1 = {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"El numero mayor es el num2 = {num2}")
    else:
        print(f"El numero mayor es el num3 = {num3}")