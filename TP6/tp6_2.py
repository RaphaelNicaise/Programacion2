from modulo_color import Color

class Borde:
    def __init__(self,grosor:int,color:Color):
        if not isinstance(color,Color):
            raise ValueError("Error al ingresar color")
        
        if not isinstance(grosor,int):
            raise ValueError("Error al ingresar grosor")
        
        self.__grosor = grosor
        self.__color = color
        
    def __str__(self):
        return f"Grosor: {self.__grosor} Color: {self.__color.obtenerRGB()}"
    
    def __repr__(self):
        return f"Borde({self.__grosor},{self.__color.__repr__()})" # repr de color = Color(r,g,b)
    
    # Comandos
    def establecerGrosor(self,grosor:int):
        if not isinstance(grosor,int):
            raise ValueError("Error al ingresar grosor")
        self.__grosor = grosor
        
    def establecerColor(self,color:Color):
        if not isinstance(color,Color):
            raise ValueError("Error al ingresar color")
        self.__color = color
    
    def copiarValores(self,bordeACopiar:'Borde'):
        if not isinstance(bordeACopiar,Borde):
            raise ValueError("Error al ingresar borde")
        
        self.__grosor = bordeACopiar.obtenerGrosor()
        self.__color = bordeACopiar.obtenerColor()
        
    # Consultas
    def obtenerGrosor(self)->int:
        return self.__grosor
    
    def obtenerColor(self)->Color:
        return self.__color
        
    def clonar(self)->'Borde':
        return eval(self.__repr__()) # repr de borde = Borde(grosor,repr de color)
    
    def esIgualQueSuperficial(self,borde:'Borde')->bool:
        if not isinstance(borde,Borde):
            raise ValueError("Error al ingresar borde")
        return self.obtenerColor() == borde.obtenerColor() and self.obtenerGrosor() == borde.obtenerGrosor()
    
class tester:
    @staticmethod
    def test1():
        
        color = Color(255,255,255)
        borde_1 = Borde(5,color)
        print("borde_1: ", borde_1)

        borde_2 = Borde(1,Color(1,1,1))
        print(borde_2)
        borde_2.copiarValores(borde_1) # Borde 2 toma los valores de borde 1
        print("borde_2: ",borde_2)

        clon_borde_2 = borde_2.clonar()
        print("clon_borde_2: ",clon_borde_2)
        
        print(clon_borde_2.esIgualQueSuperficial(borde_2)) # Da falso porque al clonar se crea un nuevo objeto Color, y por mas que sean equivalentes, no son el mismo objeto

if __name__ == "__main__":
    tester.test1()