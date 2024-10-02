import random

class Humano:
    
    MAXIMO_VIDA = 1000
    def __init__(self, nombre: str, sexo: chr, vida: float = 100):
        self._nombre = nombre
        self._vida = vida
        self._sexo = sexo
    
    def __str__(self) -> str:
        return f"Nombre: {self._nombre}, Vida: {self._vida}, Sexo: {self._sexo}"
    
    # consultas
    def obtenerNombre(self): return self._nombre
    def obtenerVida(self): return self._vida
    def obtenerSexo(self): return self._sexo
    def estaVivo(self) -> bool:
        return self._vida > 0  # Corregido el acceso a _vida
    
    def saludar(self):
        print(f"{self._nombre} está saludando")
        
    def saltar(self):
        print(f"{self._nombre} está saltando") 
    
    def recibirDanio(self, danio: int):
        self._vida -= danio
        if self._vida < 0:
            self._vida = 0 

    
class Soldado(Humano):
    
    def __init__(self, nombre: str, sexo: chr, vida: float = Humano.MAXIMO_VIDA, arma: 'Arma' = None):
        super().__init__(nombre, sexo, vida)
        self.__arma = arma
        self.__punteria = random.randint(20, 100)
        self.__vendas = 3
        
    def __str__(self) -> str:
        return f"{super().__str__()}, Puntería: {self.__punteria}, Arma: {self.__arma}"
    
    def obtenerArma(self): return self.__arma
    def obtenerPunteria(self): return self.__punteria
    
    # Comandos
    def asignarArma(self, arma: 'Arma'):
        self.__arma = arma
        self.__arma.asignarPortador(self)
        
    def quitarArma(self):
        self.__arma = None
        self.__arma.desasignarPortador(self)
        
    def disparar(self, objetivo: 'Humano'):
        if self.obtenerVida() <= 0: # Si el soldado esta muerto no puede disparar
            return
        if objetivo.obtenerVida() <= 0: # Si el objetivo esta muerto no puede recibir danio
            print(f"{objetivo.obtenerNombre()} esta muerto")
        else:
            if self.__arma: # Si el soldado tiene un arma puede disparar
                
                # TODO: Verificar si el arma tiene balas, si no tiene, se pone a recargar y salta el turno
                if self.__arma.obtenerBalas() == 0: # Si el soldado no tiene balas, recarga
                    self.__arma.recargar()
                    print(f"{self.obtenerNombre()} no dispara porque no tiene balas, ahora esta recargando su arma")
                else: # Si el soldado tiene balas, dispara
                    danio = self.__arma.calcularDanio(self.__punteria) # Calcula el danio
                    self.__arma.bajarBala() # Baja una bala
                    print(f"{self.obtenerNombre()} {chr(3)}({round(self.obtenerVida(),2)}) ha disparado a {objetivo.obtenerNombre()} {chr(3)}({round(objetivo.obtenerVida(),2)} - {danio})")
                    objetivo.recibirDanio(danio) # El objetivo recibe danio
                    if objetivo.obtenerVida() <= 0: # Si el objetivo muere
                        print(f"{objetivo.obtenerNombre()} ha muerto {"\U0001F480"}")
                        
            else:
                print("No tiene arma")   
    
    def curarse(self,curacion:int):
        if self.estaVivo():
            self._vida += curacion
            if self._vida > Soldado.MAXIMO_VIDA:
                self._vida = Soldado.MAXIMO_VIDA
    
    def usarVenda(self):
        if self.__vendas > 0:
            self.curarse(20)
            print(f"{self._nombre} se ha curado con una venda {chr(3)}({round(self.obtenerVida(),2)}+20)")
        else:
            print("No tiene mas vendas")
    
    
class Arma:
    def __init__(self, nombre: str, danio: float):
        self.__nombre = nombre
        self.__danio = danio
        self.__mira = False
        self.__portador = None
        self.__silenciador = False
        self.__limite_cargador = 0
        self.__balas = 0
        
    def __str__(self) -> str:
        return f"Arma: {self.__nombre}, Daño: {self.__danio}"
    
    def obtenerNombre(self): return self.__nombre
    
    def obtenerPortador(self): return self.__portador
    
    def asignarPortador(self, portador: 'Soldado'):
        self.__portador = portador
    
    def desasignarPortador(self):
        self.__portador = None
    
    def calcularDanio(self, punteria: int):
        danio = random.uniform(20, 40) * (punteria / 90)
        
        if not self.__mira:
            danio *= 0.5 
        
        if self.__silenciador:
            danio *= 0.8
        
        return round(danio, 2)
    
    def colocarMira(self):
        self.__mira = True
    
    def quitarMira(self):
        self.__mira = False   
    
    def colocarSilenciador(self):
        self.__silenciador = True
        
    def quitarSilenciador(self):
        self.__silenciador = False
    
    def asignarLimiteCargador(self, cantBalas: int):
        self.__limite_cargador = cantBalas
        self.__balas = cantBalas
        
    def obtenerLimiteCargador(self):
        # Obtener balas de la clase hija
        return self.__limite_cargador
    
    def obtenerBalas(self):
        return self.__balas
    
    def recargar(self):
        self.__balas = self.__limite_cargador
    
    def bajarBala(self):
        self.__balas -= 1
        

class M4(Arma):
    def __init__(self):
        super().__init__("M4", 30)
        super().asignarLimiteCargador(25)

    
class AK47(Arma):
    def __init__(self):
        super().__init__("AK47", 40)
        super().asignarLimiteCargador(30)
    
class Tester:
    @staticmethod
    def run():
        juan = Soldado("Juan", "M")
        marcos = Soldado("Marcos", "M")
        arma1 = M4()
        arma2 = AK47()
        juan.asignarArma(arma1)  # Juan tiene un arma M4
        marcos.asignarArma(arma2)  # Marcos tiene un arma AK47
        juan.obtenerArma().colocarMira()  # Juan coloca la mira a su arma
        juan.obtenerArma().colocarSilenciador()  # Juan coloca el silenciador a su arma
        
        while juan.estaVivo() and marcos.estaVivo():
            
            prob_curacion = random.randint(0,15)
            prob_quien_se_cura = random.randint(0, 1)
            
            if prob_curacion == 0:
                if prob_quien_se_cura == 0:
                    juan.usarVenda()
                else:
                    marcos.usarVenda()
            
            prob_disparador = random.randint(0, 1)
            if prob_disparador == 0: 
                juan.disparar(marcos)
                print("Balas Juan: ",juan.obtenerArma().obtenerBalas())
            else: 
                marcos.disparar(juan)
                print("Balas Marcos: ",marcos.obtenerArma().obtenerBalas())
            
                

if __name__ == "__main__":
    Tester.run()

