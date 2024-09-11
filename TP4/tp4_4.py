import random

class Automovil:
    def __init__(self, marca: str, modelo:str, anio:int, velMaxima:float, velActual: float):
        
        if velMaxima < 0 or velActual < 0:
            raise TypeError("La velocidad no puede ser negativa")
        if anio < 0:
            raise TypeError("El año no puede ser negativo")
        
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__velMaxima = velMaxima
        self.__velActual = velActual
        
    def establecerMarca(self, marca:str)->bool:
        self.__marca = marca
    
    def establecerModelo(self, modelo:str)->bool:
        self.__modelo = modelo
    
    def establecerAnio(self, anio:int)->bool:
        self.__anio = anio
    
    def establecerVelActual(self, velMaxima:float)->bool:
        self.__velMaxima = velMaxima
    
    def establecerVelMaxima(self, velocidad:float)->bool:
        self.__velActual = velocidad
    
    def acelerar(self, incrementoVel:int)->bool:
        if incrementoVel >= 0 and self.__velActual < self.__velMaxima:
            if (self.__velActual+incrementoVel) >= self.__velMaxima:
                self.__velActual = self.__velMaxima
            else:
                self.__velActual += incrementoVel
            return True
        else:
            return False

    def desacelerar(self, decrementoVel:int)->bool:
        if decrementoVel >= 0 and (self.__velActual-decrementoVel)>=0:
            self.__velActual -= decrementoVel
            return True
        else:
            return False
    
    def frenarPorCompleto(self)->bool:
        if self.__velActual != 0:
            self.__velActual = 0
            return True
        else:
            return False
        
    def obtenerMarca(self):
        return self.__marca 
    
    def obtenerModelo(self):
        return self.__modelo
    
    def obtenerAnio(self):
        return self.__anio
    
    def obtenerVelMaxima(self):
        return self.__velMaxima
    
    def obtenerVelActual(self):
        return self.__velActual
    
    def calcularMinutosParaLlegar(self, distanciaKM:float)->int:
        if self.__velActual > 0:
            minutos = distanciaKM / self.__velActual * 60
            return minutos
        elif self.__velActual == 0:
            return -1
        
        
class testAuto:
    @staticmethod
    def test1():
        Auto = Automovil("Peugeout","2008",2016,200,0)
        iteraciones = int(input("Ingresar cantidad de iteraciones a realizar: "))
        for _ in range(iteraciones):
            
            n = random.randint(0,3)
            match n:
                case 0: # acelerar(20)
                    print(f"Velocidad {Auto.obtenerVelActual()}km/h",end="")
                    if Auto.acelerar(20):
                        print(" a ",Auto.obtenerVelActual(), "km/h")
                    else:
                        print(" limite de velocidad maxima alcanzado, no se puede acelerar mas")
                case 1: 
                    print(f"Velocidad {Auto.obtenerVelActual()}km/h",end="")
                    if Auto.desacelerar(15):
                        print(" a ",Auto.obtenerVelActual(), "km/h")
                    else:
                        print(f" no se puede ir a km/h menores a 0")
                case 2: 
                    print(f"Velocidad {Auto.obtenerVelActual()}km/h",end="")
                    if Auto.frenarPorCompleto():
                        print(" a ",Auto.obtenerVelActual(), "km/h")
                    else:
                        print(f" El auto ya esta frenado")
                case 3: # calcularMinutosParaLlegar(50)
                    if Auto.calcularMinutosParaLlegar(50) == -1:
                        print("El auto esta detenido")
                    else:
                        print(f"El auto llegara en {round(Auto.calcularMinutosParaLlegar(50))} minutos")
    def test2():
        Auto = Automovil("Peugeout","2008",2016,200,0)
        iteraciones = int(input("Ingresar cantidad de iteraciones a realizar: "))
        
        for _ in range(iteraciones):
 
            n = random.randint(0,3)
            match n:
                case 0: # acelerar(de )
                    print(f"Velocidad {Auto.obtenerVelActual()}km/h",end="")
                    if Auto.acelerar(random.randint(0,30)):
                        print(" a ",Auto.obtenerVelActual(), "km/h")
                    else:
                        print(" limite de velocidad maxima alcanzado, no se puede acelerar mas")
                case 1: 
                    print(f"Velocidad {Auto.obtenerVelActual()}km/h",end="")
                    if Auto.desacelerar(random.randint(0,30)):
                        print(" a ",Auto.obtenerVelActual(), "km/h")
                    else:
                        print(f" no se puede ir a km/h menores a 0")
                case 2: 
                    print(f"Velocidad {Auto.obtenerVelActual()}km/h",end="")
                    if Auto.frenarPorCompleto():
                        print(" a ",Auto.obtenerVelActual(), "km/h")
                    else:
                        print(f" El auto ya esta frenado")
                case 3: # calcularMinutosParaLlegar(50)
                    if Auto.calcularMinutosParaLlegar(50) == -1:
                        print("El auto esta detenido")
                    else:
                        km_a_recorrer = random.randint(0,1000)
                        print(f"El auto llegara en {round(Auto.calcularMinutosParaLlegar(km_a_recorrer))} minutos si quiere hacer {km_a_recorrer}km ")
                                   
if __name__ == "__main__":
    while True:
        try:
            option = input("Desea realizar el test1 o test2? (1/2): ")
            if option == "1":
                testAuto.test1()
                break
            elif option == "2":
                testAuto.test2()
                break
        except ValueError:
            print("Ingrese un valor valido")