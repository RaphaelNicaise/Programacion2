from modulo_fecha import Fecha
import random

class Atraccion:
    def __init__(self,nombre:str,tipo:str,emocion:str,estaturaMinima:int):
        
        self.__nombre = nombre
        
        if tipo not in ['Mecanica','Electrica','Agua','Recorrido','Obra']:
            raise ValueError("Tipo incorrecto")
        self.__tipo = tipo
        
        if emocion not in ['Alta','Media','Baja']:
            raise ValueError("Emocion incorrecta")
        self.__emocion = emocion
        
        if not (0 < estaturaMinima < 300):
            raise ValueError("Estatura incorrecta")
        
        self.__estaturaMinima = estaturaMinima # en cm 
        self.__turnos = []
            
    def __str__():
        pass
    
    def __repr__():
        pass

    # Consultas
    
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerTipo(self)->str: return self.__tipo
    
    def obtenerEmocion(self)->str: return self.__emocion
    
    def obtenerEstaturaMinima(self)->int: return self.__estaturaMinima
    
    def obtenerTurnos(self)->list: return self.__turnos
    # Comandos
    
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    def establecerTipo(self,tipo:str):
        if tipo not in ['Mecanica','Electrica','Agua','Recorrido','Obra']:
            raise ValueError("Tipo incorrecto")
        self.__tipo = tipo
    
    def establecerEmocion(self,emocion:str):
        if emocion not in ['Alta','Media','Baja']:
            raise ValueError("Emocion incorrecta")
        self.__emocion = emocion
        
    def establecerTurno(self,turno:str):
        if turno not in ['Mañana','Tarde','Noche']:
            raise ValueError("Turno incorrecto")
        self.__turnos.append(turno)
        
    def desasociarTurno(self,turno:str):
        if turno in self.__turnos:
            self.__turnos.remove(turno)
        raise ValueError("Turno no encontrado")
    
    
    
class Visitante:
    def __init__(self,nombre:str,edad:int,estatura:int,correo:str=None):
        self.__nombre = nombre
        
        if not (0 < edad < 120):
            raise ValueError("Edad incorrecta")
        self.__edad = edad
        if not (0 < estatura < 300):
            raise ValueError("Estatura incorrecta")
        self.__estatura = estatura # en cm
        self.__correo = correo
        self.__entrada = []
        self.__registro_atracciones = []
        
    def __str__(self):
        return f'Visitante: {self.__nombre} - {self.__edad} - {self.__estatura} - {self.__correo}'
    
    def __repr__():
        pass

    # Consultas
    
    def obtenerNombre(self): return self.__nombre
    
    def obtenerEdad(self): return self.__edad
    
    def obtenerEstatura(self): return self.__estatura
    
    def obtenerCorreo(self): return self.__correo
    
    def obtenerEntrada(self): return self.__entrada
      
    def obtenerRegistroAtracciones(self): return self.__registro_atracciones
    # Comandos
    
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    def establecerEdad(self,edad:int):
        if 0 < edad < 120:
            self.__edad = edad
        else:
            raise ValueError("Edad incorrecta")    

    def establecerCorreo(self,correo:str):
        self.__correo = correo  
        
    def establecerEntrada(self,entrada:'Entrada'):
        if isinstance(entrada,Entrada):
            self.__entrada.append(entrada)
    
    def desasociarEntrada(self,entrada:'Entrada'):
        if isinstance(entrada,Entrada):
            self.__entrada.remove(entrada)
     
    def registrarAtraccion(self,atraccion:'Atraccion'):
        if isinstance(atraccion,Atraccion):
            self.__registro_atracciones.append(atraccion)
            
    
                
class Entrada:
    
    CONTADOR_ENTRADAS = 0
    
    def __init__(self,fecha:'Fecha',tipo:str,visitante:'Visitante'):
        Entrada.CONTADOR_ENTRADAS += 1
        self.__numero_entrada = Entrada.CONTADOR_ENTRADAS
        self.__fecha = fecha
        self.__tipo = tipo
        self.__visitante = visitante
        
        visitante.establecerEntrada(self)
        
    def __str__(self):
        return f'Entrada N°{self.__numero_entrada} - {self.__fecha} - {self.__tipo} - {self.__visitante}'
    
    def __repr__(self):
        return str(self.__numero_entrada)
    # Consultas
    
    def obtenerNumeroEntrada(self): return self.__numero_entrada
    
    def obtenerFecha(self): return self.__fecha
    
    def obtenerTipo(self): return self.__tipo
    
    def obtenerVisitante(self): return self.__visitante
    
    # Comandos
    
    def establecerFecha(self,fecha:'Fecha'):
        if isinstance(fecha,Fecha):
            self.__fecha = fecha
    
    def establecerTipo(self,tipo:str):
        if tipo in ['General','Vip']:
            self.__tipo = tipo
            
    def cambiarVisitante(self,visitante:'Visitante'):
        if isinstance(visitante,Visitante):
            self.__visitante.desasociarEntrada(self)
            self.__visitante = visitante
            visitante.establecerEntrada(self)
            
    

class GuiaDeVisitante:
    
    def __init__(self,nombre:str,turno:str):
        self.__nombre = nombre
        if turno in ['Mañana','Tarde','Noche']:
            self.__turno = turno
    
    def __str__():
        pass
    
    def __repr__():
        pass

    # Consultas
    
    def obtenerNombre(self): return self.__nombre
    
    def obtenerTurno(self): return self.__turno
    
    # Comandos
    
    def establecerTurno(self,turno:str):
        if turno not in ['Mañana','Tarde','Noche']:
            raise ValueError("Turno incorrecto")
        self.__turno = turno
        
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    
class tester:
    @staticmethod
    def run():
        pass

if __name__ == '__main__':
    try:    
        atraccion1 = Atraccion('Montaña Rusa','Mecanica','Alta',150)
        atraccion2 = Atraccion('Calesita','Mecanica','Baja',100)
        atraccion3 = Atraccion('Casa del terror','Mecanica','Media',120)
        atraccion1.establecerTurno('Mañana')
        atraccion1.establecerTurno('Tarde')
        atraccion2.establecerTurno('Tarde')
        atraccion3.establecerTurno('Mañana')
        atraccion3.establecerTurno('Tarde')
        
        guia1 = GuiaDeVisitante('Juan','Mañana')
        guia2 = GuiaDeVisitante('Pedro','Tarde')
        guia3 = GuiaDeVisitante('Maria','Tarde')
        guia4 = GuiaDeVisitante('Ana','Mañana')
        
        visitante1 = Visitante('Carlos',25,180,'carlos@gmail.com')
        visitante2 = Visitante('Lucia',30,160,'Luci@gmail.com')
        visitante3 = Visitante('Pablo',40,170,'No tiene mail')
        visitante4 = Visitante('Sofia',22,165,'sofia@gmail.com')
        visitante5 = Visitante('Miguel',35,175,'miguel@gmail.com')
        visitante6 = Visitante('Laura',28,145,'laura@gmail.com')
        
        # Visitante 1 compra dos entradas
        entrada1 = Entrada(Fecha(1,1,2020),'General',visitante1)
        entrada2 = Entrada(Fecha(2,1,2020),'General',visitante1)
        
        print(f"Entradas del visitante 1: {visitante1.obtenerEntrada()}") # 2 entradas
        print(f"Visitante que tiene la entrada 2: {entrada2.obtenerVisitante()}") # Visitante 1
        entrada2.cambiarVisitante(visitante2) # Le sacamos la entrada al visitante 1 y se la damos al visitante 2
        print(f"Entradas del visitante 1: {visitante1.obtenerEntrada()}") # 1 entrada
        print(f"Visitante que tiene la entrada 2: {entrada2.obtenerVisitante()}") # Visitante 2
       
       
        
    
    except ValueError as error:
        print(error)