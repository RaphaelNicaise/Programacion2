from Models.Entities.poliza_inmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self,numero: int, incendio: float, explosion: float, robo:float,cantPersonas: int, montoEquipamiento: float, montoInmobiliario: float, montoPersona: float):
        super().__init__(numero, incendio, explosion, robo)
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoInmobiliario = montoInmobiliario
        self.__montoPersona = montoPersona
    
    def __str__(self):
        return f"{super().__str__()}, Cantidad de personas: {self.__cantPersonas}, Monto equipamiento: {self.__montoEquipamiento}, Monto inmobiliario: {self.__montoInmobiliario}, Monto por persona: {self.__montoPersona}"
    
    @classmethod
    def fromDict(cls, dict):
        return cls(
            dict["numero"],
            dict["incendio"],
            dict["explosion"],
            dict["robo"],
            dict["cantPersonas"],
            dict["montoEquipamiento"],
            dict["montoInmobiliario"],
            dict["montoPersona"]
        )
    
    def toDict(self):
        return {
            "numero": self.getNumero(),
            "incendio": self.getIncendio(),
            "explosion": self.getExplosion(),
            "robo": self.getRobo(),
            "cantPersonas": self.__cantPersonas,
            "montoEquipamiento": self.__montoEquipamiento,
            "montoInmobiliario": self.__montoInmobiliario,
            "montoPersona": self.__montoPersona
        }
    
        
    # Getters
    def getCantPersonas(self) -> int:
        return self.__cantPersonas
    
    def getMontoEquipamiento(self) -> float:
        return self.__montoEquipamiento
    
    def getMontoInmobiliario(self) -> float:
        return self.__montoInmobiliario
    
    def getMontoPersona(self) -> float:
        return self.__montoPersona
    
    # Setters
    
    def setCantPersonas(self, cantPersonas: int):
        self.__cantPersonas = cantPersonas
        
    def setMontoEquipamiento(self, montoEquipamiento: float):
        self.__montoEquipamiento = montoEquipamiento
        
    def setMontoInmobiliario(self, montoInmobiliario: float):
        self.__montoInmobiliario = montoInmobiliario
        
    def setMontoPersona(self, montoPersona: float):
        self.__montoPersona = montoPersona
        
    def valorMensualPoliza(self)->float:
        return super().getIncendio()*0.01 + super().getExplosion()*0.01 + super().getRobo()*0.02 + self.__montoEquipamiento*0.01 + self.__montoInmobiliario*0.01 + (self.__montoPersona*self.__cantPersonas)*0.01
    
    