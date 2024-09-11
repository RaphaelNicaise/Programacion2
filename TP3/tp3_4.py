"""
Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo 
las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por 
el usuario, utilizando list comprehensions.
"""
palabras = dict({
    "Python": "Lenguaje interpretado y de propósito general.",
    "Java": "Lenguaje orientado a objetos y multiplataforma.",
    "C": "Lenguaje de programación de bajo nivel y alto rendimiento.",
    "JavaScript": "Lenguaje usado principalmente para desarrollo web.",
    "Ruby": "Lenguaje dinámico, enfocado en la simplicidad.",
    "PHP": "Lenguaje de script para desarrollo web del lado del servidor.",
    "Go": "Lenguaje compilado y concurrente desarrollado por Google.",
    "Swift": "Lenguaje de Apple para desarrollo en iOS y macOS.",
    "Kotlin": "Lenguaje moderno para desarrollo en Android.",
    "Rust": "Lenguaje centrado en la seguridad y el rendimiento."
})

print("Lista de palabras")
for i in palabras.keys():
    print(i)
    
def palabras_con_letra(letra:str):
    palabras_con_letra = [palabra for palabra in palabras.keys() if i[0] == letra.upper()]
    return palabras_con_letra 
while True:
    letra = input("Ingrese una letra -> ")    
    if letra:
        print(palabras_con_letra("p"))
        break
    
