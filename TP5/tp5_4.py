from tp5_3 import Color

class testColores:
    @staticmethod
    def test():
    #a
        color_1 = Color() 
        print(color_1)
        color_2 = Color(70, 70, 70)
        print(color_2) 
        color_3 = Color(255, 255, 255)
        print(color_3)  
        print(color_1.esIgualQue(color_2))
        print(color_2.esIgualQue(color_3)) 
        color_4 = color_1
        print(color_4) 
        color_5 = color_2.clonar()
        print(color_5)
        # b
        color_6 = Color(140,250,140)
        print(color_6) 
        color_4 = color_6
        print(color_4) 
        color_2 = color_5.clonar()
        print(color_2) 
        print(color_2.esIgualQue(color_5)) 
        color_3 = color_2
        print(color_3) 
        color_1 = color_5.complemento()
        print(color_1) 
        # c 
        color_1 = color_5.complemento() 
        color_2 = color_5.clonar()
        print(color_2)  
        color_3 = color_2
        print(color_3) 
 
if __name__ == '__main__':
    testColores.test()