from soldado import Soldado
from arma import M4, AK47
import random 
import time

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
            else: 
                marcos.disparar(juan)
                
            time.sleep(0.5)
            
if __name__ == "__main__":
    Tester.run()