# En CMD ~ FOR /L %i IN (1,1,#cantidaddepuntos) DO type nul > tp_%i.py

"""
Implemente una función que, dada una lista de números, devuelva una nueva lista que contenga 
el cuadrado de cada número utilizando list comprehensions. 
"""

lista = [33,44,66,12,51,23]

def lista_cuadrado(lista:list)->list:
    lista_cuadrado = [elemento**2 for elemento in lista] 
    return lista_cuadrado

print(lista_cuadrado(lista))