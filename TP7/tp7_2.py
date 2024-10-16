from abc import ABC,abstractmethod

class Propietario:
    def __init__(self,nombre,telefono,edad):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__edad = edad
        
    def __repr__(self):
        return self.__nombre
class Inmueble(ABC):
    def __init__(self,codigo:int,domicilio:str,propietario: 'Propietario',metrosCuadrados:int,estado:int):
        if not isinstance(codigo,int) or codigo < 1: raise ValueError
        if not isinstance(domicilio,str): raise ValueError
        if not isinstance(propietario,Propietario): raise ValueError
        if not isinstance(metrosCuadrados,int): raise ValueError
        if not isinstance(estado,int): raise ValueError
        
        self._codigo = codigo
        self._domicilio = domicilio
        self._propietario = propietario
        self._metrosCuadrados = metrosCuadrados
        self._estado = estado
        
    def __str__(self):
        return f'{self._codigo} - {self._domicilio} - {self._propietario} - {self._metrosCuadrados} - {self._estado}'    

    def __repr__(self):
        return str(self._codigo)
    # Comandos
    
    def establecerDomicilio(self,domicilioNuevo:str):
        self._domicilio = domicilioNuevo
        
    def establecerPropietario(self,propietarioNuevo:'Propietario'):
        if not isinstance(propietarioNuevo,Propietario): raise ValueError
        self._propietario = propietarioNuevo
    
    def establecerMetrosCuadrados(self,metrosCuadradosNuevos:int):
        if metrosCuadradosNuevos < 1: raise ValueError
        self._metrosCuadrados = metrosCuadradosNuevos
        
    def establecerEstado(self,estadoNuevo:int):
        if estadoNuevo < 1: raise ValueError
        self._estado = estadoNuevo
        
    
    # Consultas
    
    def obtenerCodigo(self)->int: return self._codigo
    
    def obtenerDomicilio(self)->str: return self._domicilio
    
    def obtenerPropietario(self)->'Propietario': return self._propietario
    
    def obtenerMetrosCuadrados(self)->int: return self._metrosCuadrados
    
    def obtenerEstado(self)->int: return self._estado
    
    @abstractmethod
    def costoAlquiler(self,base: int)->float:
        pass
    
    @abstractmethod
    def precioVenta(self,m2:float)->float:
        pass
    
    
class Departamento(Inmueble):
    def __init__(self,codigo:int,domicilio:str,propietario: 'Propietario',metrosCuadrados:int,estado:int,gastosComunes:float,cochera:bool):
        
        if not isinstance(gastosComunes,float | int) or gastosComunes < 0: raise ValueError
        if not isinstance(cochera,bool): raise ValueError
        
        super().__init__(codigo,domicilio,propietario,metrosCuadrados,estado)
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera
    
    # Comandos
    
    def establecerGastosComunes(self,gastos:float):
        if not isinstance(gastos,float | int) or gastos < 0: raise ValueError
        self.__gastosComunes = gastos
    
    def establecerCochera(self,cochera:bool):
        if not isinstance(cochera,bool): raise ValueError
        self.__cochera = cochera
        
    # Consultas
    def obtenerCochera(self)->bool: return self.__cochera
    def obtenerGastosComunes(self)->float: return self.__gastosComunes
    
    def costoAlquiler(self,base: int)->float:
        
        return (base + self.__gastosComunes * self.obtenerMetrosCuadrados())* (1.3 if self.__cochera else 1)
    
    def precioVenta(self,m2:float)->float:
        
        return m2 * self.obtenerEstado() + self.__gastosComunes * (1.5 if self.__cochera else 1) 
    
class Quinta(Inmueble):
    def __init__(self,codigo:int,domicilio:str,propietario: 'Propietario',metrosCuadrados:int,estado:int,metrosParque:int):
        if not isinstance(metrosParque,int) or metrosParque < 1: raise ValueError
        super().__init__(codigo,domicilio,propietario,metrosCuadrados,estado)
        self.__metrosParque = metrosParque
    
    # Comandos
    
    def establecerMetrosParque(self,metros:int):
        if not isinstance(metros,int) or metros < 1: raise ValueError
        self.__metrosParque = metros
        
    # Consultas
    
    def obtenerMetrosParque(self)->int: return self.__metrosParque
    
    def costoAlquiler(self,base: int)->float:
        
        return base + self.obtenerMetrosParque() * 10
    
    def precioVenta(self,m2:float)->float:
        
        return m2 * self.obtenerEstado() + self.obtenerMetrosParque() * 20
       
class Tester:
    @staticmethod
    def run():
        pass
    
if __name__ == '__main__':
    Tester.run()