from abc import ABC,abstractmethod
from color import Color

class Vehiculo(ABC):
    
    TIPOS = ["nafta","diésel","eléctrico"]
    
    def __init__(self, marca:str, patente:str, color:'Color', anio:int, precio:float, combustible:str,kilometraje:int=0):
        
        if not isinstance(marca,str):
            raise ValueError("Marca debe ser un string")
        if not isinstance(patente,str):
            raise ValueError("Patente debe ser un string")
        if not isinstance(color,Color):
            raise ValueError("Color debe ser un objeto de tipo Color")
        if not isinstance(anio,int) or anio < 1900:
            raise ValueError("Año debe ser un entero")
        if not isinstance(precio,float) or precio < 0:
            raise ValueError("Precio debe ser un float")
        if not isinstance(combustible,str):
            raise ValueError("Combustible debe ser un string")
        if combustible not in Vehiculo.TIPOS:
            raise ValueError("Combustible debe ser nafta, diésel o eléctrico")
        
        self._marca = marca
        self._patente = patente
        self._color = color
        self._anio = anio
        self._precio = precio
        self._tipoCombustible = combustible
        self._kilometraje = kilometraje
        
    @abstractmethod
    def __str__(self):
        pass
      
    # Comandos
    
    def setMarca(self, marca:str):
        if not isinstance(marca,str):
            raise ValueError("Marca debe ser un string")
        self._marca = marca
    
    def setPatente(self, patente:str):
        if not isinstance(patente,str):
            raise ValueError("Patente debe ser un string")
        self._patente = patente
        
    def setColor(self, color:'Color'):
        if not isinstance(color,Color):
            raise ValueError("Color debe ser un objeto de tipo Color")
        self._color = color
    
    def setAnio(self, anio:int):
        if not isinstance(anio,int):
            raise ValueError("Año debe ser un entero")
        self._anio = anio
        
    def setPrecio(self, precio:float):
        if not isinstance(precio,float) or precio < 0:
            raise ValueError("Precio debe ser un float mayor a 0")
        self._precio = precio
        
    def setCombustible(self, combustible:str):
        
        if not isinstance(combustible,str):
            raise ValueError("Combustible debe ser un string")
        if combustible not in Vehiculo.TIPOS:
            raise ValueError("Combustible debe ser nafta, diésel o eléctrico")
        self._combustible = combustible
        
    
    # Consultas
    
    def getMarca(self)->str:
        return self.__marca
    
    def getPatente(self)->str:
        return self.__patente
    
    def getColor(self)->'Color':
        return self.__color
    
    def getAnio(self)->int:
        return self.__anio
    
    def getPrecio(self)->float:
        return self.__precio
    
    def getCombustible(self)->str:
        return self.__combustible
    
    def getKilometraje(self)->int:
        return self.__kilometraje
    
class Autos(Vehiculo):
    def __init__(self, marca:str, patente:str, color:'Color', anio:int, precio:float, combustible:str,kilometraje:int=0, puertas:int=4, aireAcondicionado:bool=True):
        if not isinstance(puertas,int) or puertas < 0:
            raise ValueError("Puertas debe ser un entero mayor a 0")
        
        super().__init__(marca, patente, color, anio, precio, combustible, kilometraje)
        self.__puertas = puertas
        self.__aireAcondicionado = aireAcondicionado
    
    def __str__(self):
        return f"Marca: {self._marca}\nPatente: {self._patente}\nColor: {self._color.obtenerNombreColor()}\nAño: {self._anio}\nPrecio: {self._precio}\nCombustible: {self._tipoCombustible}\nKilometraje: {self._kilometraje}\nPuertas: {self.__puertas}\nAire Acondicionado: {self.__aireAcondicionado}"
        
    # Comandso
    
    def setPuertas(self, puertas:int):
        if not isinstance(puertas,int) or puertas < 0:
            raise ValueError("Puertas debe ser un entero mayor a 0")
        self.__puertas = puertas
    
    def setAireAcondicionado(self, aireAcondicionado:bool):
        if not isinstance(aireAcondicionado,bool):
            raise ValueError("Aire acondicionado debe ser un booleano")
        
        self.__aireAcondicionado = aireAcondicionado
        
    # Consultas
    
    def getPuertas(self)->int:
        return self.__puertas
    
    def getAireAcondicionado(self)->bool:
        return self.__aireAcondicionado
    
    
    
class Motos(Vehiculo):
    def __init__(self, marca:str, patente:str, color:'Color', anio:int, precio:float, combustible:str,cilindrada:int,ancho_manubrio:int,kilometraje:int=0):
        
        if not isinstance(cilindrada,int) or cilindrada < 0:
            raise ValueError("Cilindrada debe ser un entero mayor a 0")
        if not isinstance(ancho_manubrio,int) or ancho_manubrio < 0:
            raise ValueError("Ancho de manubrio debe ser un entero mayor a 0")
        
        super().__init__(marca, patente, color, anio, precio, combustible, kilometraje)
        self.__cilindrada = cilindrada
        self.__ancho_manubrio = ancho_manubrio
    
    def __str__(self):
        return f"Marca: {self._marca}\nPatente: {self._patente}\nColor: {self._color.obtenerNombreColor()}\nAño: {self._anio}\nPrecio: {self._precio}\nCombustible: {self._tipoCombustible}\nKilometraje: {self._kilometraje}\nCilindrada: {self.__cilindrada}\nAncho de manubrio: {self.__ancho_manubrio}"
    
    # Comandos
    
    def setCilindrada(self, cilindrada:int):
        if not isinstance(cilindrada,int) or cilindrada < 0:
            raise ValueError("Cilindrada debe ser un entero mayor a 0")
        
        self.__cilindrada = cilindrada
        
    def setAnchoManubrio(self, ancho_manubrio:int):
        if not isinstance(ancho_manubrio,int) or ancho_manubrio < 0:
            raise ValueError("Ancho de manubrio debe ser un entero mayor a 0")
        
        self.__ancho_manubrio = ancho_manubrio
    
    # Consultas
    
    def getCilindrada(self)->int:
        return self.__cilindrada
    
    def getAnchoManubrio(self)->int:
        return self.__ancho_manubrio
    
class Tester:
    @staticmethod
    def run():
        rojo = Color(255,32,32)
        auto = Autos("Ford","ABC123",rojo,2000,100000.0,"nafta",0,4,True)
        moto = Motos("Yamaha","DEF456",rojo,2010,50000.0,"nafta",250,50)
        print(auto)
        print(moto)
        
if __name__ == "__main__":
    Tester.run()