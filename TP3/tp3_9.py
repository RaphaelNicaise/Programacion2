"""
Dada una lista de números, crea dos listas separadas: una que contenga los 
números pares y otra que contenga los números impares utilizando list 
comprehensions.
"""
n=50
pares = [i for i in range(0,n) if i % 2 == 0]
impares = [i for i in range(0,n) if i % 2 != 0]
print(f"Pares : {pares}")
print(f"Impares : {impares}")


