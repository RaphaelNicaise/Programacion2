class Especie:
    
    def __init__(self,nombre:str) -> None:
        self.__nombre = nombre
        self.__machos = 0
        self.__hembras = 0
        self.__ritmo = 0.0
        
    def __str__(self) -> str:
        return f"Especie {self.__nombre} Machos: {self.__machos}  Hembras: {self.__hembras}"
    
    # Consultas Triviales
    
    def obtenerMachos(self):
        return self.__machos
    
    def obtenerHembras(self):
        return self.__hembras
    
    def obtenerRitmo(self):
        return self.__ritmo
    
    # Consultas
    

    def poblacionActual(self)->int:
        return self.__machos + self.__hembras
    
    def poblacionEstimada(self,anios:int)->int:
        pass
    
    def aniosParaPoblacion(self,poblacion:int)->int:
        pass
    
    def riesgo(self)->str:
        pass
    
    def masHembras(self)->bool:
        pass
    
    def mayorRitmo(self,otraEspecie:'Especie')->'Especie':
        if self.__ritmo > otraEspecie.obtenerRitmo():
            return self
        elif self.__ritmo < otraEspecie.obtenerRitmo():
            return otraEspecie
        else:
            print("Especies tienen el mismo ritmo")
            
    def clonar(self)->'Especie': 
        return self
    
    def toString()->str:
        pass
    
    # Comandos
    def establecerHembras(self,cantHembras:int):
        if cantHembras >= 0:
            self.__hembras = cantHembras
    
    def establecerMachos(self,cantMachos:int):
        if cantMachos >= 0:
            self.__machos = cantMachos
    
    def establecerRitmo(self,ritmo:float):
        self.__ritmo = ritmo
    
    
    def actualizarHembras(self, cantHembras: int):
        if self.__hembras + cantHembras >= 0:
            self.__hembras += cantHembras
        else:
            print("no se puede tener una cantidad negativa de especimenes")
    
    def actualizarMachos(self,cantMachos:int):
        if self.__hembras + cantMachos >= 0:
            self.__hembras += cantMachos
        else:
            print("no se puede tener una cantidad negativa de especimenes")
        
    def actualizarRitmo(self, ritmo:float):
        self.__ritmo = ritmo
    
class testEspecies:
    @staticmethod
    def test():
        pass
    
if __name__ == '__main__':
    testEspecies.test()
    
