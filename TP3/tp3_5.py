"""
Dado un rango de números, crea una lista que contenga todos los números primos 
dentro de ese rango utilizando list comprehensions.
"""

minimo,maximo=2,100                 # FUNCION ALL DEVUELVE TRUE SI TODOS LOS ELEMENTOS DEL BUCLE CUMPL
                                    # CUMPLEN LA CONDICION                   
primos = [i for i in range(minimo, maximo) if all(i % j != 0 for j in range(2, i))]

print(primos)   
        
         