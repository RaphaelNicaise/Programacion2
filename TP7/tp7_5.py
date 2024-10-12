from abc import ABC,abstractmethod

# TODO Diagrama de clases

class Personal(ABC):
    def __init__(self,nombre:str,apellido:str,dni:str,legajo:str):
    
        for i in [nombre,apellido,dni,legajo]:
            if not isinstance(i,str) or i.isspace():
                raise ValueError("Un argumento es erroneo")
        
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni    
        self._legajo = legajo
     
    @abstractmethod
    def __str__(self):
        pass 
    
    # Comandos
    
    def setNombre(self,nombre:str):
        if not isinstance(nombre,str) or nombre.isspace():
            raise ValueError("nombre mal ingresado")
        
        self._nombre = nombre
    
      
    def setApellido(self,apellido):
        if not isinstance(apellido,str) or apellido.isspace():
            raise ValueError("apellido mal ingresado")
        
        self._apellido = apellido
    
         
    def setDNI(self,dni):
        if not isinstance(dni,str) or dni.isspace():
                raise ValueError("DNI mal ingresado")
        self._dni = dni
   
    def setLegajo(self,legajo):
        
        if not isinstance(legajo,str) or legajo.isspace():
            raise ValueError("Legajo mal ingresado")
        self._legajo = legajo
        
    # Consultas
    
    def getNombre(self)->str:
        return self._nombre
    
    def getApellido(self)->str:
        return self._apellido
    
    def getDNI(self)->str:
        return self._apellido
    
    def getLegajo(self)->str:
        return self.__legajo
    
class Administrativo(Personal):
    def __init__(self, nombre:str, apellido:str, dni:str, legajo:str):
        super().__init__(nombre, apellido, dni, legajo)
    
    def __str__(self):
        return f"Administrativo:  {self._nombre} {self._apellido} {self._dni} {self._legajo}"
class Programador(Personal):
    def __init__(self, nombre:str, apellido:str, dni:str, legajo:str, proyecto:str):
        super().__init__(nombre, apellido, dni, legajo)

        if not isinstance(proyecto,str) or proyecto.isspace():
            raise ValueError("Proyecto mal ingresado")
        
        self.__proyecto = proyecto
    
    def __str__(self):
        return f"Programador:  {self._nombre} {self._apellido} {self._dni} {self._legajo} {self.__proyecto}"
    
    # Comandos
    
    def setProyecto(self,proyecto:str):
        
        if not isinstance(proyecto,str) or proyecto.isspace():
            raise ValueError("Proyecto mal ingresado")
        
        self.__proyecto = proyecto
        
    # Consultas
    
    def getProyecto(self)->str:
        return self.__proyecto
    
    
class Manteninimiento(Personal):
    def __init__(self, nombre:str, apellido:str, dni:str, legajo:str, area:str):
        super().__init__(nombre, apellido, dni, legajo)
        
        if not isinstance(area,str) or area.isspace():
            raise ValueError("Area mal ingresada")
        
        self.__area = area
    
    def __str__(self):
        return f"Mantenimiento:  {self._nombre} {self._apellido} {self._dni} {self._legajo} {self.__area}"
    # Comandos
    
    def setArea(self,area):
        
        if not isinstance(area,str) or area.isspace():
            raise ValueError("Area mal ingresada")
        
        self.__area = area
    
    # Consultas

    def getArea(self):
        return self.__area

class Tester:
    @staticmethod
    def run():
        try:
            empleado_1 = Personal("Raphael","Nicaise","2894352","22363")
        except TypeError as e:
            print(e)
        
        administrativa_1 = Administrativo("Martina","Barrios","12341234","23442")
        print(administrativa_1)
        
        programador_1 = Programador("Raphael","Nicaise","2894352","22363","Proyecto1")
        print(programador_1)
        
        manteninimiento_1 = Manteninimiento("Hugo","Gonzalez","12341234","23442","Area 1")
if __name__ == "__main__":
    Tester.run()