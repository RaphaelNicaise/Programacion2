from tp7_2 import Inmueble, Departamento, Quinta, Propietario

class Inmobiliaria:
    def __init__(self):
        self.__propiedades:Inmueble = []
    
    # Comandos
    def insertar(self,inmueble:'Inmueble'):
        if not isinstance(inmueble,Inmueble): raise ValueError
        if self.estaInmueble(inmueble.obtenerCodigo()): raise ValueError("Ya existe este inmueble en la inmobiliaria")
        self.__propiedades.append(inmueble)
    
    def eliminar(self, inmueble:'Inmueble'):
        if not isinstance(inmueble,Inmueble): raise ValueError
        if not self.estaInmueble(inmueble.obtenerCodigo()): raise ValueError("No existe este inmueble")
        self.__propiedades.remove(inmueble)
        
    # Consultas
    
    def estaInmueble(self,codigo: int)->bool:
        for propiedad in self.__propiedades:
            if propiedad.obtenerCodigo() == codigo:
                return True
        return False
    
    def estaInmueble(self,inmueble:'Inmueble')->bool:
        for propiedad in self.__propiedades:
            if propiedad == inmueble:
                return True    
        
    def esIgual(self, inmueble:'Inmueble')->bool:
        pass
    
    def hayInmuebles(self)->bool:
        return self.__propiedades != []
    
    def contarPropiedadesMasMetros(self,metros:int)->int:
        """
        cuenta la cantidad de propiedades que tienen menos metros que el valor pasado por parametro
        """
        cuenta = 0
        for propiedades in self.__propiedades:
            if propiedades.obtenerMetros() < metros:
                cuenta += 1
            
        return cuenta
            
    def mayorPrecioVenta(self)->int:
        """
        Devuelve el precio de venta de la propiedad con mayor precio de venta
        """
        mayor = 0
        for propiedad in self.__propiedades:
            if propiedad.precioVenta() > mayor:
                mayor = propiedad.precioVenta()
        return mayor
    
    def costoMenorQue(self, monto:int)->list:
        """
        devuelve la lista de propiedades que tienen un costo de alquiler menor al monto pasado por parametro
        """
        lista = []
        
        for propiedad in self.__propiedades:
            if propiedad.costoAlquiler() < monto:
                lista.append(propiedad)
                
        return lista
    
    def obtenerPropiedades(self)->list:
        return self.__propiedades
class Tester:
    @staticmethod
    def run():
        propietario1 = Propietario('Raul',12345678,18)
        inmueble1 = Departamento(1,'Calle Falsa 123',propietario1,100,1,1000.0,True) 
        propietario2 = Propietario('Juan',87654321,25)
        inmueble2 = Departamento(2,'Calle Falsa 124',propietario2,200,2,2000.0,False)
        
        inmobiliaria = Inmobiliaria()
        inmobiliaria.insertar(inmueble1)
        inmobiliaria.insertar(inmueble2)
        print(inmueble1)
        print(inmueble2)
        
        print(inmobiliaria.obtenerPropiedades())
        
        
if __name__ == '__main__':
    Tester.run()