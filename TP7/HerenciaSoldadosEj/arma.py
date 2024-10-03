import random

class Arma:
    def __init__(self, nombre: str, danio: float):
        self._nombre = nombre
        self._danio = danio
        self._mira = False
        self._portador = None
        self._silenciador = False
        self._limite_cargador = 0
        self._balas = 0
        
    def __str__(self) -> str:
        return f"Arma: {self._nombre}, Daño: {self._danio}"
    
    # Consultas
    def obtenerNombre(self): return self._nombre
    
    def obtenerPortador(self): return self._portador
    
    def obtenerLimiteCargador(self): return self._limite_cargador
    
    def obtenerBalas(self): return self._balas
    
    # Comandos
    
    def asignarPortador(self, portador):
        
        self._portador = portador
    
    def desasignarPortador(self):
        self._portador = None
    
    def calcularDanio(self, punteria: int):
        danio = random.uniform(20, 40) * (punteria / 90)
        
        if not self._mira:
            danio *= 0.5 
        
        if self._silenciador:
            danio *= 0.8
        
        return round(danio, 2)
    
    def colocarMira(self):
        if not self._mira:
            self._mira = True
        else: 
            print("Ya tiene mira")
            
    def quitarMira(self):
        if self._mira:
            self._mira = False
        else:
            print("No tiene mira") 
    
    def colocarSilenciador(self):
        self._silenciador = True
        
    def quitarSilenciador(self):
        self._silenciador = False
    
    def asignarLimiteCargador(self, cantBalas: int):
        self._limite_cargador = cantBalas
        self._balas = cantBalas
    
    def recargar(self):
        self._balas = self._limite_cargador
    
    def bajarBala(self):
        self._balas -= 1

class M4(Arma):
    def __init__(self):
        super().__init__("M4", 30)
        super().asignarLimiteCargador(20)
        
    
class AK47(Arma):
    def __init__(self):
        super().__init__("AK47", 40)
        super().asignarLimiteCargador(30)