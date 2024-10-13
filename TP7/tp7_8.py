from abc import ABC,abstractmethod

class Cuenta(ABC):
    def __init__(self,DNI:str,tasaDeInteres:float,comisionMensual:float,saldoInicial:float=0):
        if not isinstance(DNI,str):
            raise ValueError("El DNI debe ser un string")
        if not isinstance(tasaDeInteres,float) or tasaDeInteres < 0:
            raise ValueError("La tasa de interes debe ser un numero positivo")
        if not isinstance(comisionMensual,float) or comisionMensual < 0:
            raise ValueError("La comision mensual debe ser un numero positivo")
        if not isinstance(saldoInicial,float) or saldoInicial < 0:
            raise ValueError("El saldo inicial debe ser un numero positivo")
            
        self._DNI = DNI
        self._saldo = saldoInicial
        self._retiros_este_mes = 0
        self._depositos_este_mes = 0
        self._tasaDeInteres = tasaDeInteres
        self._comisionMensual = comisionMensual
        
    def __str__(self):
        return f"DNI {self._DNI} - Saldo: {self._saldo} - Retiros este mes: {self._retiros_este_mes} - Depositos este mes: {self._depositos_este_mes} - Tasa de interes: {self._tasaDeInteres} - Comision mensual: {self._comisionMensual}"
    
    # Comandos
    
    @abstractmethod
    def depositar(self,monto):
        pass
    
    @abstractmethod
    def retirar(self,monto):
        pass
    
    @abstractmethod
    def extractoMensual(self):
        pass
    
    def setSaldo(self,saldo):
        if not isinstance(saldo,float) or saldo < 0:
            raise ValueError("El saldo debe ser un numero positivo")
        self._saldo = saldo
    
    def setTasaDeInteres(self,tasaDeInteres):
        if not isinstance(tasaDeInteres,float) or tasaDeInteres < 0:
            raise ValueError("La tasa de interes debe ser un numero positivo")
        self._tasaDeInteres = tasaDeInteres
        
    def setComisionMensual(self,comisionMensual):
        if not isinstance(comisionMensual,float) or comisionMensual < 0:
            raise ValueError("La comision mensual debe ser un numero positivo")
        self._comisionMensual = comisionMensual
        
    # Consultas
    
    def getSaldo(self):
        return self._saldo
    
    def getRetirosEsteMes(self):
        return self._retiros_este_mes
    
    def getDepositosEsteMes(self):
        return self._depositos_este_mes
    
    def getTasaDeInteres(self):
        return self._tasaDeInteres
    
    def getComisionMensual(self):
        return self._comisionMensual    
    
class CtaCte(Cuenta):
    def __init__(self,DNI:str,tasaDeInteres:float,comisionMensual:float,saldoInicial:float=0):
        super().__init__(DNI,tasaDeInteres,comisionMensual,saldoInicial)
        
        self.__limiteDescubierto = 0 # Limite negativo
        self.__penalizaciones = 0
        
    def __str__(self):
        return super().__str__() + f" - Limite descubierto: {self.__limiteDescubierto} - Penalizaciones: {self.__penalizaciones}"
    
    # Comandos
    
    def setLimiteDescubierto(self,limiteDescubierto):
        if not isinstance(limiteDescubierto,float) or limiteDescubierto < 0 :
            raise ValueError("El limite descubierto debe ser un numero")
        self.__limiteDescubierto = limiteDescubierto
        
    def depositar(self,monto):
        if monto < 0:
            raise ValueError("El monto a depositar debe ser positivo")
        
        adeudado = 0
        
        if self._saldo < 0:
            adeudado = -self._saldo
        
        self._saldo += monto - adeudado*0.02
            
    def retirar(self,monto):
        if self._saldo - monto < -(self.__limiteDescubierto):
            raise ValueError("No se puede retirar mas dinero del permitido")
        self._saldo -= monto
        if self._saldo < 0:
            self.penalizar()
    
    def extractoMensual(self):
        pass
        
    def penalizar(self):
        self.__penalizaciones += 1
    
    # Consultas
    
    def getLimiteDescubierto(self):
        return self.__limiteDescubierto
    
    def getPenalizaciones(self):
        return self.__penalizaciones
    
    
class CajaDeAhorro(Cuenta):
    def __init__(self,DNI:str,tasaDeInteres:float,comisionMensual:float,saldoInicial:float=0):
        super().__init__(DNI,tasaDeInteres,comisionMensual,saldoInicial)
        self.__activa = True
    
    def __str__(self):
        return super().__str__() + f" - Activa: {self.__activa}"
    
    # Comandos
    
    def depositar(self,monto):
        if not self.__activa:
            raise ValueError("La cuenta esta desactivada")
        self._saldo += monto
        self._depositos_este_mes += 1    
    
    def retirar(self,monto):
        if not self.__activa:
            raise ValueError("La cuenta esta desactivada")
        
        comision = 0
        
        if self._retiros_este_mes > 4:
            comision = 1000
            
        self._saldo -= monto - comision
        self._retiros_este_mes += 1
        
        if self._saldo < 0:
            self.__desactivar()
            
    def extractoMensual(self):
        pass
    
    def activar(self):
        if self.__activa:
            raise ValueError("La cuenta ya esta activa")
        self.__activa = True
        
    def desactivar(self):
        if not self.__activa:
            raise ValueError("La cuenta ya esta desactivada")
        self.__activa = False
        
    # Consultas
    
    def getActiva(self):
        return self.__activa
    
class Banco:
    @staticmethod
    def run():
        cuenta1 = CtaCte("12345678",0.1,1000.0,10000.0)
        print(cuenta1)
        cuenta1.retirar(10000)
        try:
            cuenta1.retirar(1000)
        except ValueError as e:
            print(e)
        
        cuenta1.setLimiteDescubierto(4000.0)
        print(cuenta1)
        cuenta1.retirar(4000)
        print(cuenta1)
        cuenta1.depositar(5000)
        print(cuenta1)
        
    
if __name__ == "__main__":
    Banco.run()
    