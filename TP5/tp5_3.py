import requests

class Color:
    def __init__(self,rojo:int=255,verde:int=255,azul:int=255):
        
        for color in [rojo,verde,azul]:
            if not isinstance(color,int) or color > 255 or color < 0:
                raise ValueError("Error al ingresar valor")
            
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
        
    def __str__(self)->str:
        return f"Color: {self.obtenerNombreColor()} RGB:({self.__rojo},{self.__verde},{self.__azul})"
    
    # Consultas
    def obtenerRojo(self)->int:
        return self.__rojo
    
    def obtenerVerde(self)->int:
        return self.__verde
    
    def obtenerAzul(self)->int:
        return self.__azul
    
    def obtenerRGB(self)->tuple:
        return self.__rojo,self.__verde,self.__azul
    
    def obtenerNombreColor(self)->str:
        url = f"https://www.thecolorapi.com/id?rgb=rgb({self.__rojo},{self.__verde},{self.__azul})"
        color_data = requests.get(url).json()
        
        nombre = color_data['name']['value']
        hex_mas_cercano = color_data['name']['closest_named_hex']
        
        return f"{nombre} ({hex_mas_cercano})"
    
    def esRojo(self)->bool:
        """
        retorna el valor verdadero si el objeto que recibe el mensaje representa el color rojo
        Returns:
            bool: _description_
        """
        """
        Es un rojo si el valor de rojo es mayor al de verde y al de azul agregandole con una diferencia
        para evitar que por un minimo de rojo se defina como rojo
        """
        return self.__rojo > self.__verde + 40 and self.__rojo > self.__azul + 40
        
    
    def esGris(self)->bool:
        """
        retorna el valor verdadero si el objeto que recibe el mensaje representa el color gris
        Returns:
            bool: _description_
        """
        no_son_extremos = 0 < self.__rojo < 255 and 0 < self.__verde < 255 and 0 < self.__azul < 255
        colores_iguales = self.__rojo == self.__azul == self.__verde
        if colores_iguales and no_son_extremos:
            return True
        else:
            return False
        
    
    def esNegro(self)->bool:
        """
        retorna el valor verdadero si el objeto que recibe el mensaje representa el color negro
        Returns:
            bool: _description_
        """
        return self.__rojo == 255 and self.__verde == 255 and self.__azul == 255
    
    def complemento(self)->'Color':
        """
        retorna un nuevo objeto con el color complemento del color 
        del objeto que recibe el mensaje para alcanzar el color blanco.
        Returns:
            Color: _description_
        """
        rojo_compl = 255 - self.__rojo
        verde_compl = 255 - self.__verde
        azul_compl = 255 - self.__azul
        
        return Color(rojo_compl,verde_compl,azul_compl)
            
    def esIgualQue(self, otroColor:'Color')->bool:
        """
        retorna el valor verdadero si ambos objetos son equivalentes.
        Args:
            otroColor (Color): _description_
        Returns:
            bool: _description_
        """
        if not self.__rojo == otroColor.obtenerRojo():
            return False    
        if not self.__verde == otroColor.obtenerVerde():
            return False
        if not self.__azul == otroColor.obtenerAzul():
            return False
        
        return True
    
    def clonar(self)->'Color': # Crear otro objeto con los colores de la instancia
        """
        devuelve un nuevo color con el mismo estado interno que el color que recibe el mensaje
        Returns:
            Color: _description_
        """
        return Color(self.__rojo,self.__verde,self.__azul)
    
    # Comandos
    def variar(self,val:int):
        """
        modifica cada componente de color sumándole si es 
        posible, un valor dado. Si sumándole el valor dado a una o varias 
        componentes se supera el valor 255, dicha componente queda en 255. Si el 
        argumento es negativo la operación es la misma pero en ese caso el mínimo 
        valor que puede tomar una componente, es 0.
        Logica aplicada en las funciones de variar cada color
        Args:
            val (int): _description_
        """
        self.variarRojo(val)
        self.variarVerde(val)
        self.variarAzul(val)
        
                       
    def variarRojo(self,val:int):
        """
        modifica al componente de rojo sumándole un valor dado
        Args:
            val (int): _description_
        """
        if val > 0:
            if self.__rojo + val < 255:
                self.__rojo += val
            else:
                self.__rojo = 255
        elif val < 0:
            if self.__rojo + val > 0:
                self.__rojo += val # val seria un un numero negativo
            else:
                self.__rojo = 0
            
    def variarVerde(self,val:int):
        """
        modifica al componente de verde sumándole un valor dado
        Args:
            val (int): _description_
        """
        if val > 0:
            if self.__verde + val < 255:
                self.__verde += val
            else:
                self.__verde = 255
        elif val < 0:
            if self.__verde + val > 0:
                self.__verde += val
            else:
                self.__verde = 0
    
    def variarAzul(self,val:int):
        """
        modifica al componente de azul sumándole un valor dado
        Args:
            val (int): _description_
        """
        if val > 0:
            if self.__azul + val < 255:
                self.__azul += val
            else:
                self.__azul = 255
        elif val < 0:
            if self.__azul + val > 0:
                self.__azul += val
            else:
                self.__azul = 0
    
    def establecerRojo(self,val:int):
        if (255 >= val >= 0):
            self.__rojo = val
    
    def establecerVerde(self,val:int):
        if (255 >= val >= 0):
            self.__verde = val
    
    def establecerAzul(self,val:int):
        if (255 >= val >= 0):
            self.__azul = val
    
    def copiar(self,otroColor:'Color'): 
        """
        agarra los colores de una instancia del objeto, y se los asigna a self
        Args:
            otroColor (Color): _description_
        """
        self.__rojo = otroColor.obtenerRojo()
        self.__verde = otroColor.obtenerVerde()
        self.__azul = otroColor.obtenerAzul()
    
    
class testColores:
    @staticmethod
    def test():
        try:
            colorError = Color(23,123,"a")
        except ValueError as e:
            print(e)
        
        color_1 = Color(azul=43) # 255 255 43
        
        color_2 = Color()
        if not color_2.esGris(): # False
            print(f"Color_2 esta en la escala de grises pero no cuenta como gris porque (es Negro: {color_2.esNegro()})")
        
        color_3 = Color(233,233,233)
        if color_3.esGris(): # True
            print("Color_3 es un gris") 
        
        complemento_color_3 = color_3.complemento()
        print("color_3:",color_3.obtenerRGB())
        print("complemento_color_3:",complemento_color_3.obtenerRGB())
        
        color_4 = Color(233,233,233)
        if color_4.esIgualQue(color_3):
            print("color_4 y color_3 son equivalentes")
        else:
            print("color_4 y color_3 no son equivalentes")
            
        clon_color_1 = color_1.clonar()
        if color_1.esIgualQue(clon_color_1):
            print("el clon de color_1 y color_1 son equivalentes") 
            
        color_5 = Color(99,64,223) 
        print("Color_5: ",color_5.obtenerRGB())
        color_5.variar(120)
        print("Color_5 variado 120: ",color_5.obtenerRGB())
        color_5.variar(-220)
        print("Color_5 variado -220: ",color_5.obtenerRGB())
                
        color_6 = Color() # Se crea 255,255,255 pero quiere tomar los valores de color_5
        color_6.copiar(color_5)
        print("Color_5 -> ",color_5)
        print("Color_6 -> ",color_6)  
        
if __name__ == "__main__":
    testColores.test()