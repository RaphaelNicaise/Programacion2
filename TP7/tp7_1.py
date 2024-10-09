class Aseguradora:
    def __init__(self):
        self.__seguros = []

    def __str__(self):
       pass
    
    # Comandos
    
    def insertar(self,poliza: 'PolizaInmueble'):
        self.__seguros.append(poliza)
        self.__seguros.sort(key=PolizaInmueble.obtenerNumero)
    
    def eliminar(self,poliza: 'PolizaInmueble'):
        self.__seguros.remove(poliza)
    
    # Consultas
    
    def obtenerSeguros(self):
        return self.__seguros
    
    def existePoliza(self,poliza: 'PolizaInmueble')->bool:
        return poliza in self.__seguros
    
    def hayPolizas(self)->bool:
        return self.__seguros is not None
    
    def costoTotal(self)->float:
        costo_total = 0
        
        for seguro in self.__seguros:
            costo_total += seguro.costoPoliza()
            
        return costo_total    

    def esIgual(self,aseguradora: 'Aseguradora'):
        return self.obtenerSeguros() == aseguradora.obtenerSeguros()
        
class PolizaInmueble:
    def __init__(self,numero:int,incendio:float,explosion:float,robo:float):
        if not isinstance(numero,int) and numero < 0: raise ValueError
        
        if not isinstance(incendio,float) and incendio < 0: raise ValueError
        
        if not isinstance(explosion,float) and explosion < 0: raise ValueError
        
        if not isinstance(robo,float) and robo < 0: raise ValueError
        
        self.__numero = numero
        self.__incendio = incendio
        self.__explosion = explosion
        self.__robo = robo

    def __str__(self):
        return self.__numero
    
    def __repr__(self):
        return str(self.__numero)
    # Comandos
    
    def establecerIncendio(self,incendioNuevo:float):
        self.__incendio = incendioNuevo
        
    def establecerExplosion(self,explosionNuevo:float):
        self.__explosion = explosionNuevo
        
    def establecerRobo(self,roboNuevo:float):
        self.__robo = roboNuevo
    
    # Consultas
    
    def costoPoliza(self)->float:
        return self.__incendio + self.__explosion + self.__robo
    
    def obtenerNumero(self)->int:
        return self.__numero
    
    def obtenerIncendio(self)->float:
        return self.__incendio
    
    def obtenerExplosion(self)->float:
        return self.__explosion
    
    def obtenerRobo(self)->float:
        return self.__robo
           
        
class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, numero:int, incendio:float, explosion:float, robo:float,cantPersonas:int,montoEquipamiento:float,montoMobiliario:float,montoPersona:float):
        super().__init__(numero, incendio, explosion, robo)
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoMobiliario = montoMobiliario
        self.__montoPersona = montoPersona
    
    def __repr__(self):
        return super().__repr__()
    
    # Comandos
    
    def establecerCantPersonas(self,cantPersonas:int):
        if not isinstance(cantPersonas,int) or cantPersonas < 0: raise ValueError
        self.__cantPersonas = cantPersonas
        
    def establecerMontoEquipamiento(self,montoEquipamiento:float):
        if not isinstance(montoEquipamiento,[float,int]) or montoEquipamiento < 0: raise ValueError
        self.__montoEquipamiento = montoEquipamiento
        
    def establecerMontoMobiliario(self,montoMobiliario:float):
        if not isinstance(montoMobiliario,[float,int]) or montoMobiliario < 0: raise ValueError
        self.__montoMobiliario = montoMobiliario
        
    def establecerMontoPersona(self,montoPersona:float):
        if not isinstance(montoPersona,[float,int]) or montoPersona < 0: raise ValueError
        self.__montoPersona = montoPersona
    
    # Consultas
    
    def obtenerCantPersonas(self)->int:
        return self.__cantPersonas
    
    def obtenerMontoEquipamiento(self)->float:
        return self.__montoEquipamiento
    
    def obtenerMontoMobiliario(self)->float:
        return self.__montoMobiliario
    
    def obtenerMontoPersona(self)->float:
        return self.__montoPersona
    
    def costoPoliza(self)->float:
        return super().costoPoliza() + self.__cantPersonas * self.__montoPersona + self.__montoEquipamiento + self.__montoMobiliario 
        # Costo poliza = costo poliza clase padre (inmueble) + costo por persona + costo equipamiento + costo mobiliario
        
class Tester:
    @staticmethod
    def run():
        aseguradora_1 = Aseguradora()
        aseguradora_2 = Aseguradora()
        
        poliza_1 = PolizaInmueble(1,1000,2000,3000)
        poliza_2 = PolizaInmueble(2,1000,2000,3000)
        poliza_3 = PolizaInmueble(3,1000,1500,7000)
        poliza_4 = PolizaInmuebleEscolar(4,1000,1500,7000,80,2000,3000,4000)
        poliza_5 = PolizaInmuebleEscolar(5,1000,1500,7000,120,2000,3000,4000)
        
        print(f"Seguros Aseguradora 1:{aseguradora_1.obtenerSeguros()}")
        aseguradora_1.insertar(poliza_2) # Insertamos poliza numero 2
        print(f"Seguros Aseguradora 1:{aseguradora_1.obtenerSeguros()}") # [2]
        aseguradora_1.insertar(poliza_1) # Insertamos poliza numero 1 y se ordena la lista
        print(f"Seguros Aseguradora 1:{aseguradora_1.obtenerSeguros()}") # [1,2] 
        
        print(f"Costo total aseguradora 1:{aseguradora_1.costoTotal()}") # Costo Total de las polizas en la aseguradora 1 -> 12000
        
        aseguradora_2.insertar(poliza_1)
        aseguradora_2.insertar(poliza_2)
        
        print(f"Las 2 aseguradoras mismas polizas:{aseguradora_1.esIgual(aseguradora_2)}") # Las aseguradoras 1 y 2 son iguales -> True
        
        aseguradora_1.insertar(poliza_3) # Insertamos poliza 3 en aseguradora 1
        
        print(f"Las 2 aseguradoras mismas polizas:{aseguradora_1.esIgual(aseguradora_2)}") # ya no son iguales
        
        aseguradora_1.eliminar(poliza_1) # Eliminamos poliza 1 de aseguradora 1
        
        print(f"Existe poliza 1 en aseguradora 1:{aseguradora_1.existePoliza(poliza_1)}") # False
        print(f"Hay polizas en aseguradora 1:{aseguradora_1.hayPolizas()}") # True
        print(f"Seguros Aseguradora 1:{aseguradora_1.obtenerSeguros()}") # [2,3]

        print(f"Poliza 4:{poliza_4.costoPoliza()}")
        print(f"Poliza 5:{poliza_5.costoPoliza()}")
        
if __name__ == '__main__':
    Tester.run()