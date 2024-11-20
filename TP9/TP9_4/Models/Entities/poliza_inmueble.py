class PolizaInmueble:
    def __init__(self,numero: int, incendio: float, explosion: float, robo:float):
        self.__numero = numero
        self.__incendio = incendio
        self.__explosion = explosion
        self.__robo = robo
    
    def __str__(self):
        return f"Numero: {self.__numero}, Incendio: {self.__incendio}, Explosion: {self.__explosion}, Robo: {self.__robo}"
        
    @classmethod
    def fromDict(cls, dict)->"PolizaInmueble":
        return cls(
            dict["numero"],
            dict["incendio"],
            dict["explosion"],
            dict["robo"]
        )    

    def toDict(self):
        return {
            "numero": self.__numero,
            "incendio": self.__incendio,
            "explosion": self.__explosion,
            "robo": self.__robo
        }
        
    def valorMensualPoliza(self)->float:
        return self.__incendio*0.02 + self.__explosion*0.01 + self.__robo*0.03
    
    # Setters
    
    def setNumero(self, numero: int):
        self.__numero = numero
        
    def setIncendio(self, incendio: float):
        self.__incendio = incendio
    
    def setExplosion(self, explosion: float):
        self.__explosion = explosion
    
    def setRobo(self, robo: float):
        self.__robo = robo
        
    # Getters
    
    def getNumero(self) -> int:
        return self.__numero
    
    def getIncendio(self) -> float:
        return self.__incendio
    
    def getExplosion(self) -> float:
        return self.__explosion
    
    def getRobo(self) -> float:
        return self.__robo
    
