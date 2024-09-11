"""
Realizar un programa que pida los tres lados de un triángulo e indique el tipo de 
triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos 
lados iguales) o Escaleno (tres lados distintos). 
"""

lado1 = float(input("lado 1: "))
lado2 = float(input("lado 2: "))
lado3 = float(input("lado 3: "))

if lado1 >= 0 or lado2 >= 0 or lado3 >= 0: 
    if lado1 == lado2 and lado2 == lado3:
        print("Equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Isosceles") 
    elif lado1 != lado2 != lado3:
        print("Escaleno")
    else:
        print("Triangulo no valido")    
else:
    print("No se permiten valores negativos")    
    



