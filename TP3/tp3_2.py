"""
Implemente una función que, dada una lista de nombres, devuelva una nueva lista 
que contenga solo los nombres que tengan una longitud mayor o igual a una 
cantidad de caracteres pasada por parámetro, utilizando list comprehensions. 
"""

nombres = ["Raphael","Nicolas","Emma","Martin","Jose","Damian","Fernando"]

def nombres_mas_largos_que_n(nombres:list,n:int):
    nombres_mas_largos_que_n = [
        nombre for nombre in nombres if len(nombre)>=n
    ]
    return nombres_mas_largos_que_n
    
print(nombres_mas_largos_que_n(nombres,7))