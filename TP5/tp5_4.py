from tp5_3 import Color

class testColores:
    @staticmethod
    def test():
    #a
        color_1 = Color() 
        color_2 = Color(70, 70, 70) 
        color_3 = Color(255, 255, 255) 
        igualdad1 = color_1.esIgualQue(color_2) 
        igualdad2 = color_2.esIgualQue(color_3) 
        color_4 = color_1 
        color_5 = color_2.clonar()
        # b
        color_6 = Color(140,250,140) 
        color_4 = color_6 
        color_2 = color_5.clone() 
        igualdad3 = color_2.esIgualQue(color_5) 
        color_3 = color_2 
        color_1 = color_5.complemento() 
        # c 
        color_1 = color_5.complemento() 
        color_2 = color_5.clone() 
        color_3 = color_2 
 
