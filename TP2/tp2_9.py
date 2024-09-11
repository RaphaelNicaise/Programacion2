"""
Un profesor almacenó los datos de los alumnos de su materia en un archivo 
alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas 
finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de 
legajo.  
En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de 
legajo, apellido y nombre de cada uno. 
En ambos archivos los datos están separados por punto y coma  ( ; )  . 
Desea escribir un programa para generar un archivo Promoción.txt con los apellidos 
y nombres de los alumnos que promocionan la materia, esto es, alumnos que el 
promedio de las tres notas supere los 7 puntos.  
El archivo debe quedar ordenado alfabéticamente 
"""
def leer_archivo_notas()->list:
    notas_alumnos = []
    with open("alumnos_notas.txt","r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            legajo,oral,escrito,tps=linea.strip().split(';')
            alumno_notas = dict(legajo=legajo,nota_oral=int(oral),nota_escrito=int(escrito),nota_tps=int(tps))
            notas_alumnos.append(alumno_notas)
    
    return notas_alumnos

def leer_archivo_info()->list:
    info_alumnos = []
    with open("alumnos_info.txt","r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            legajo,apellido,nombre = linea.strip().split(';')
            info_alumno = dict(legajo=legajo,apellido=apellido,nombre=nombre)
            info_alumnos.append(info_alumno)
    return info_alumnos

def obtener_nombre_alumno(legajo:str,info_alumnos:list)->str:
    for alumno in info_alumnos:
        if alumno['legajo']==str(legajo):
            return f"{alumno['apellido']} {alumno['nombre']}"

def alumnos_promocionados(notas_alumnos:list)->list:
    notas_alumnos = leer_archivo_notas()
    alumnos_promocionados = []
    for alumno_n in notas_alumnos:
        nota_final = (alumno_n['nota_oral']+alumno_n['nota_escrito']+alumno_n['nota_tps'])/3
        if nota_final >= 7:
            alumnos_promocionados.append(obtener_nombre_alumno(alumno_n['legajo'],info_alumnos)) 
    return alumnos_promocionados

def escribir_archivo_promocion(alumnos_promocionados:list):
    with open("promocion.txt","w") as archivo:
        for alumno in alumnos_promocionados:
            archivo.write(alumno+"\n")

    
notas_alumnos = leer_archivo_notas()
info_alumnos = leer_archivo_info()        
print(notas_alumnos)
print(info_alumnos)
print(obtener_nombre_alumno(1234,info_alumnos))
promocionados = alumnos_promocionados(notas_alumnos)
promocionados.sort()
print(promocionados)
escribir_archivo_promocion(promocionados)

   
