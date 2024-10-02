from modulo_color import Color

class Borde:
    def __init__(self, grosor: int, color: Color):
        """
        Inicializa un objeto Borde con un grosor y un color.

        :param grosor: El grosor del borde.
        :param color: El color del borde.
        :raises ValueError: Si el grosor no es un entero o el color no es una instancia de Color.
        """
        if not isinstance(color, Color):
            raise ValueError("Error al ingresar color")
        
        if not isinstance(grosor, int):
            raise ValueError("Error al ingresar grosor")
        
        self.__grosor = grosor
        self.__color = color
        
    def __str__(self):
        """
        Retorna una representación en cadena del objeto Borde.

        :return: Una cadena que representa el borde.
        """
        return f"Grosor: {self.__grosor} Color: {self.__color.obtenerRGB()}"
    
    def __repr__(self):
        """
        Retorna una representación oficial del objeto Borde.

        :return: Una cadena que representa el borde.
        """
        return f"Borde({self.__grosor},{self.__color.__repr__()})"
    
    def establecerGrosor(self, grosor: int):
        """
        Establece el grosor del borde.

        :param grosor: El nuevo grosor del borde.
        :raises ValueError: Si el grosor no es un entero.
        """
        if not isinstance(grosor, int):
            raise ValueError("Error al ingresar grosor")
        self.__grosor = grosor
        
    def establecerColor(self, color: Color):
        """
        Establece el color del borde.

        :param color: El nuevo color del borde.
        :raises ValueError: Si el color no es una instancia de Color.
        """
        if not isinstance(color, Color):
            raise ValueError("Error al ingresar color")
        self.__color = color
    
    def copiarValores(self, bordeACopiar: 'Borde'):
        """
        Copia los valores de otro objeto Borde.

        :param bordeACopiar: El borde del cual copiar los valores.
        :raises ValueError: Si bordeACopiar no es una instancia de Borde.
        """
        if not isinstance(bordeACopiar, Borde):
            raise ValueError("Error al ingresar borde")
        
        self.__grosor = bordeACopiar.obtenerGrosor()
        self.__color = bordeACopiar.obtenerColor()
        
    def obtenerGrosor(self) -> int:
        """
        Obtiene el grosor del borde.

        :return: El grosor del borde.
        """
        return self.__grosor
    
    def obtenerColor(self) -> Color:
        """
        Obtiene el color del borde.

        :return: El color del borde.
        """
        return self.__color
        
    def clonar(self) -> 'Borde':
        """
        Crea una copia del objeto Borde.

        :return: Una nueva instancia de Borde con los mismos valores.
        """
        return eval(self.__repr__())
    
    def esIgualQueSuperficial(self, borde: 'Borde') -> bool:
        """
        Compara superficialmente si dos bordes son iguales.

        :param borde: El borde a comparar.
        :return: True si los bordes son superficialmente iguales, False en caso contrario.
        :raises ValueError: Si borde no es una instancia de Borde.
        """
        if not isinstance(borde, Borde):
            raise ValueError("Error al ingresar borde")
        return self.__color == borde.obtenerColor() and self.__grosor == borde.obtenerGrosor()
    
    def esIgualProfundo(self, borde: 'Borde') -> bool:
        """
        Compara profundamente si dos bordes son iguales.

        :param borde: El borde a comparar.
        :return: True si los bordes son profundamente iguales, False en caso contrario.
        :raises ValueError: Si borde no es una instancia de Borde.
        """
        if not isinstance(borde, Borde):
            raise ValueError("Error al ingresar borde")
        
        return borde.obtenerColor().esIgualQue(self.__color)

class tester:
    @staticmethod
    def test1():
        """
        Realiza una serie de pruebas con la clase Borde.
        """
        color = Color(255, 255, 255)
        borde_1 = Borde(5, color)
        print("borde_1: ", borde_1)

        borde_2 = Borde(1, Color(1, 1, 1))
        print(borde_2)
        borde_2.copiarValores(borde_1)  # Borde 2 toma los valores de borde 1
        print("borde_2: ", borde_2)

        clon_borde_2 = borde_2.clonar()
        print("clon_borde_2: ", clon_borde_2)
        
        print(clon_borde_2.esIgualQueSuperficial(borde_2))  # Da falso porque al clonar se crea un nuevo objeto Color, y por mas que sean equivalentes, no son el mismo objeto
        print(clon_borde_2.esIgualProfundo(borde_2))  # Da verdadero porque se compara el contenido de los objetos Color
        
if __name__ == "__main__":
    tester.test1()