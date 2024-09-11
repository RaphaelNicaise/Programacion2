"""
Dado un diccionario de personas y sus edades, crea una lista que contenga solo los 
nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, 
utilizando list comprehensions. 
"""

personas=dict(
    roman=18,
    raphael=19,
    ulises=20,
    agustin=21,
    martina=30
)

for persona in personas.items():
    print(persona)

def obtener_personas_mayor_a_edad(edad:int)->list:
    personas_mayores_a_edad = [nombre for nombre,edad_persona in personas.items() if edad_persona>edad]
    return personas_mayores_a_edad

personas_mayores_a_edad = obtener_personas_mayor_a_edad(20)
print(personas_mayores_a_edad)