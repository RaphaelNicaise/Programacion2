"""
Escriba un programa que permita cargar una lista de alumnos junto con su nota del 
parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego 
de ingresados los datos debe generar una lista donde figure si aprobaron o no (se 
aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente 
(el resultado no se almacena, se calcula): 
ALUMNOS       PARCIAL  RESULTADO 
Smith, Juan      70    Aprobado 
Suárez, María    35    Desaprobado 
"""

def crear_lista_alumnos()->list:

    lista_alumnos_notas = []
    
    while True:
        nombre = input("Ingrese Nombre (q para salir) -> ")
        if nombre.lower() == "q":
            break  
        apellido = input("Ingrese Apellido -> ") 
        while True:
            try:
                nota_parcial = int(input("Ingrese nota de parcial -> "))
                break
            except ValueError:
                print("Error al ingresar nota de parcial")
        lista_alumnos_notas.append({'nombre':nombre,'apellido':apellido,'nota':nota_parcial})
        
    return lista_alumnos_notas

def mostar_lista(lista_alumnos:list):
    print("Alumnos              Parcial            Resultado")
    for alumno in lista_alumnos:
        if alumno['nota'] >= 40:
            resultado = "Aprobado"
        else: 
            resultado = "Desaprobado"
        print(f"{alumno['apellido']}, {alumno['nombre']}",end="")
        print(f"{alumno['nota']} {resultado}")

lista_alumnos = crear_lista_alumnos()

if lista_alumnos:
    mostar_lista(lista_alumnos)