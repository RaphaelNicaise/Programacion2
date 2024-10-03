class Humano:
    
    MAXIMO_VIDA = 100
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