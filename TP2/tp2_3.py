"""
Escriba un programa que permita cargar las notas de exámenes, primero debe 
permitir ingresar por teclado la cantidad de notas que desea cargar, y luego 
cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e 
indicar en qué índice del arreglo se encuentra. 
"""

def cargar_notas()->list:
    notas = []
    
    while True:
        try:
            cant_notas = int(input("Ingrese cantidad de notas a insertar -> "))
            if cant_notas > 0:
                break
        except ValueError:
            print("Error al ingresar numero")
    
    
    for i in range(cant_notas):
        while True:
            try:
                nota = int(input(f"Ingrese nota {i+1} -> "))
                if nota >= 1 and nota <= 10:
                    notas.append(nota)
                    break
            except ValueError:
                print("Error al ingresar nota. Por favor, ingrese un número válido.")
                continue
    return notas

notas = cargar_notas()
print(f" Esta es la lista de notas -> {notas}")