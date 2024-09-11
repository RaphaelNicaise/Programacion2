"""
9. Se desea realizar una aplicación que solicite al usuario tres números enteros 
positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén 
entre A y B inclusive.  
"""
X = int(input("Ingrese numero para buscar sus multiplos entre A Y B: ")) # 2
A = int(input("Ingrese primer numero: ")) # 1
B = int(input("Ingrese numero limite: ")) # 10

for i in range(A,B+1): # 1 2 3 4 5 6 7 8 9 10
    if i % X == 0: print(f"{i} es multiplo de 6")