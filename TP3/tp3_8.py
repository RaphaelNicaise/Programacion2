"""
Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los 
elementos únicos utilizando list comprehensions.
"""
lista = [1,2,3,4,5,1,2,3,1,2,3]
elementos_unicos = [numero for numero in lista if lista.count(numero) == 1]
print(f"Lista de elementos unicos -> {elementos_unicos}")