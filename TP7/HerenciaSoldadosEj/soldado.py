from humano import Humano
from arma import Arma
import random


class Soldado(Humano):
    
    def __init__(self, nombre: str, sexo: chr, vida: float = Humano.MAXIMO_VIDA, arma: 'Arma' = None):
        super().__init__(nombre, sexo, vida)
        self.__arma = arma
        self.__punteria = random.randint(20, 100)
        self.__vendas = 3
        
    def __str__(self) -> str:
        return f"{super().__str__()}, Puntería: {self.__punteria}, Arma: {self.__arma}"
    # Consultas
    
    def obtenerArma(self): return self.__arma
    def obtenerPunteria(self): return self.__punteria
    def obtenerVendas(self): return self.__vendas
    
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
                
                if self.__arma.obtenerBalas() == 0: # Si el soldado no tiene balas, recarga
                    self.__arma.recargar()
                    print(f"{self.obtenerNombre()} no dispara porque no tiene balas, ahora esta recargando su arma")
                else: # Si el soldado tiene balas, dispara
                    danio = self.__arma.calcularDanio(self.__punteria) # Calcula el danio
                    self.__arma.bajarBala() # Baja una bala
                    print(f"{self.obtenerNombre()} {chr(3)}({round(self.obtenerVida(),2)}) ha disparado con {self.__arma.obtenerNombre()}({self.__arma.obtenerBalas()}) a {objetivo.obtenerNombre()} {chr(3)}({round(objetivo.obtenerVida(),2)} - {danio})")
                    objetivo.recibirDanio(danio) # El objetivo recibe danio
                    if objetivo.obtenerVida() <= 0: # Si el objetivo muere
                        print(f"{objetivo.obtenerNombre()} ha muerto {"\U0001F480"}")
                        
            else:
                print("No tiene arma")   
    
    def usarVenda(self):
        if self.__vendas > 0:
            curacion = Soldado.MAXIMO_VIDA * 0.2
            self.curarse(curacion)
            print(f"{self._nombre} se ha curado con una venda {chr(3)}({round(self.obtenerVida(),2)}+{curacion})")
        else:
            print("No tiene mas vendas")
            
    def curarse(self,curacion:int):
        if self.estaVivo():
            self._vida += curacion
            if self._vida > Soldado.MAXIMO_VIDA:
                self._vida = Soldado.MAXIMO_VIDA