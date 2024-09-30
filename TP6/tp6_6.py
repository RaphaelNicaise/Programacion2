class Participante:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = []

    def __str__(self):
        return f"Nombre: {self.__nombre} Edad: {self.__edad} Nacionalidad: {self.__nacionalidad}"
    
    def __repr__(self):
        return f"({self.__nombre})"
    
    # Comandos
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    def establecerEdad(self,edad:int):
        self.__edad = edad
        
    def establecerNacionalidad(self,nacionalidad:int):
        self.__nacionalidad = nacionalidad
    
    def agregarDisciplina(self,disciplina:'Disciplina'):
        if not isinstance(disciplina,Disciplina):
            raise ValueError("Error al ingresar la disciplina")
        
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)    
            disciplina.agregarParticipante(self)
            
    # Consultas
    
    def obtenerNombre(self)->str: return self.__nombre

    def obtenerEdad(self)->int: return self.__edad
    
    def obtenerNacionaldiad(self)->str: return self.__nacionalidad
        
    def obtenerDisciplinas(self)->list: return self.__disciplinas
        
class Disciplina:
    def __init__(self,nombre:str,descripcion:str):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = []
    
    def __str__(self):
        return f'Disciplina: {self.__nombre} Descripcion: {self.__descripcion} Participantes: {len(self.__participantes)}'
    
    def __repr__(self):
        return f'({self.__nombre},{self.__descripcion})'
    
    # Comandos
    
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    def establecerDescripcion(self,descripcion:str):
        self.__descripcion = descripcion
    
    def agregarParticipante(self,participante:'Participante'):
        if participante not in self.__participantes:
            self.__participantes.append(participante)
    # Consultas
    
    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerDescripcion(self)->str:
        return self.__descripcion
    
    def obtenerParticipantes(self)->list:
        return self.__participantes
    
        
class tester:
    @staticmethod
    def run():
        
        futbol = Disciplina("Futbol","11v11 Pelota Redonda")
        basket = Disciplina("Basket","5v5 Pelota Redonda")
        rugby = Disciplina("Rugby","15v15 Pelota Ovalada")
        participante_1 = Participante("Raphael",19,"Frances")
        
        
        print(participante_1)
        print(participante_1.obtenerDisciplinas())
        participante_1.agregarDisciplina(futbol)
        participante_1.agregarDisciplina(rugby)
        print(participante_1.obtenerDisciplinas())
        print(futbol.obtenerParticipantes()) #
        
        participante_2 = Participante("Roman",19,"Argentino")
        
        participante_2.agregarDisciplina(basket)
        participante_2.agregarDisciplina(futbol)
        participante_2.agregarDisciplina(basket) # No lo agrega porque ya esta en las disciplinas del participante
        print(participante_2.obtenerDisciplinas())
        print(futbol.obtenerParticipantes()[0])
        
if __name__ == "__main__":
    tester.run()