"""
Dada una lista de diccionarios que contienen información de estudiantes de una 
materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final) , 
utilizando list comprehensions: 

    a. Crea una lista que contenga los nombres de todos los estudiantes. Salida 
    ejemplo: nombres: ['Pepe', 'María', 'Pedro', 'Ana'] 
    b. Crea una lista que contenga los nombres de todos los estudiantes que han 
    obtenido una calificación superior a 70 en todos los exámenes 
    c. Crea una lista que contenga los nombres de todos los estudiantes que han 
    obtenido una calificación inferior a 60 en al menos un examen.
    
"""

estudiantes = [
    {"nombre_apellido":"Raphael Nicaise","legajo":"22366","nota_parcial1":7,"nota_parcial2":9,"nota_parcial3":8},
    {"nombre_apellido":"Pepe Argento","legajo":"12341","nota_parcial1":4,"nota_parcial2":5,"nota_parcial3":4},
    {"nombre_apellido":"Guillermo Franccela","legajo":"52345","nota_parcial1":6,"nota_parcial2":6,"nota_parcial3":3},
    {"nombre_apellido":"Lionel Messi","legajo":"19301","nota_parcial1":9,"nota_parcial2":8,"nota_parcial3":10},
    {"nombre_apellido":"Michael Fox","legajo":"95192","nota_parcial1":4,"nota_parcial2":6,"nota_parcial3":9},
    {"nombre_apellido":"Freddie Mercury","legajo":"25692","nota_parcial1":6,"nota_parcial2":4,"nota_parcial3":5}
]
   
nombres = [estudiante['nombre_apellido'] for estudiante in estudiantes]
print(nombres)

estudiantes_notas_mayor_7 = [estudiante['nombre_apellido'] for estudiante in estudiantes
        if(estudiante['nota_parcial1'] >= 7 and
           estudiante['nota_parcial2'] >= 7 and
           estudiante['nota_parcial3'] >= 7)                      
]
print(estudiantes_notas_mayor_7)

estudiantes_notas_menor_6 = [estudiante['nombre_apellido'] for estudiante in estudiantes
        if(estudiante['nota_parcial1'] <= 6 or
           estudiante['nota_parcial2'] <= 6 or
           estudiante['nota_parcial3'] <= 6)                      
]
print(estudiantes_notas_menor_6)


