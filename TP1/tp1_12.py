"""
Escriba un programa que permita el ingreso de números enteros positivos, 
finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de 
menor a mayor. 
"""
n = 1
lista = []
while n > 0:
    n = int(input("Ingrese numeros (finaliza con 0) -> ")) 
    if n > 0:
        lista.append(n)
    
ordenada = True

for i in range(len(lista)-1):
    if lista[i] > lista[i+1]:
        ordenada = False

print("Tamaño de lista",len(lista))
print(lista)

if ordenada: print("La lista esta ordenada de menor a mayor")
else: print("La lista no esta ordenada de menor a mayor")
