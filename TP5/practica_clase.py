import random

class RobotDeBatalla:
    
    __MAX_ENERGIA=100
    __MIN_ENERGIA=0
    __MAX_VIDA=100
    __MIN_VIDA=0
    __MAX_ACCION=50
    __MIN_ACCION=0
    
    def __init__(self,nombre:str):
        self.__nombre = nombre
        self.__energia = RobotDeBatalla.__MAX_ENERGIA
        self.__vida = RobotDeBatalla.__MAX_VIDA
        self.__ataque = random.randint(20,RobotDeBatalla.__MAX_ACCION)
        self.__defensa = random.randint(10,RobotDeBatalla.__MAX_ACCION)
        
            
    def __str__(self):
        return f"{self.__nombre} -"

    # Consultas 
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEnergia(self)->int:
        return self.__energia
    
    def obtenerVida(self)->int:
        return self.__vida
    
    def obtenerAtaque(self)->int:
        return self.__ataque
    
    def obtenerDefensa(self)->int:
        return self.__defensa

    def estaVivo(self)->bool:
        return self.__vida > 0

    # Comandos

    def atacar(self,otroRobot:'RobotDeBatalla'):
        pass
    
    def recibirDanio
            
    def recargarEnergia(self):
        if self.estaVivo():
            self.__energia = RobotDeBatalla.__MAX_ENERGIA
    
    def establecerNombre(self,nombre:str):
        if self.estaVivo():
            self.__nombre = nombre
    
    def establecerAtaque(self,valor:int):
        if self.estaVivo():
            if RobotDeBatalla.__MIN_ACCION <= valor <= RobotDeBatalla.__MAX_ACCION:
                self.__ataque = valor
            else:
                raise ValueError()
    
    def establecerDefensa(self,valor:int):
        if self.estaVivo():
            if RobotDeBatalla.__MIN_ACCION <= valor <= RobotDeBatalla.__MAX_ACCION:
                self.__defensa = valor
            else:
                raise ValueError()
    
    def establecerVida(self,valor:int):
        if self.estaVivo():
            if RobotDeBatalla.__MIN_VIDA <= valor <= RobotDeBatalla.__MAX_VIDA:
                self.__defensa = valor
            else:
                raise ValueError()
    
    def establecerEnergia(self,valor:int):
        if self.estaVivo():                
            if RobotDeBatalla.__MIN_ENERGIA <= valor <= RobotDeBatalla.__MAX_ENERGIA:
                self.__energia = valor
            else:
                raise ValueError("El valor energia tiene que ser mayor a 0 y menor a 100")


robot1 = RobotDeBatalla("Wallie")
