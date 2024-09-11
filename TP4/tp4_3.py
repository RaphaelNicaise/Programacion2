class Vinoteca:
    CAPADICAD_MAXIMA = 5000
    def __init__(self, cantJugos:int=CAPADICAD_MAXIMA,cantBlancos:int=CAPADICAD_MAXIMA,cantTintosJovenes:int=CAPADICAD_MAXIMA,cantTintosAnejados:int=CAPADICAD_MAXIMA):
        self.__cantJugos = cantJugos
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados
    
    def reponerJugos(self):
        self.__cantJugos = Vinoteca.CAPADICAD_MAXIMA
            
    def reponerVinosBlancos(self):
        self.__cantBlancos = Vinoteca.CAPADICAD_MAXIMA   
    
    def reponerVinosTintosJovenes(self):
        self.__cantTintosJovenes = Vinoteca.CAPADICAD_MAXIMA
    
    def reponerVinosTintosAnejados(self):
        self.__cantTintosAnejados = Vinoteca.CAPADICAD_MAXIMA
    
    def venderJugos(self, n:int)->bool:
        if n > 0:
            if n > self.__cantJugos:
                n = self.__cantJugos
                print(f"Solo se vendieron {n} ya que la cantidad ingresada excede a lo que tenemos")
            self.__cantJugos -= n
            return True
        else: 
            return False
    def venderVinosBlancos(self, n:int)->bool:
        if n > 0:
            if n > self.__cantBlancos:
                n = self.__cantBlancos
                print(f"Solo se vendieron {n} ya que la cantidad ingresada excede a lo que tenemos")
                
            self.__cantJugos -= n
            return True
        else: 
            return False
    
    def venderVinosTintosJovenes(self, n:int)->bool:
        if n > 0:
            if n > self.__cantTintosJovenes:
                n = self.__cantTintosJovenes
                print(f"Solo se vendieron {n} ya que la cantidad ingresada excede a lo que tenemos")
            self.__cantJugos -= n
            return True
        else: 
            return False
    def venderVinosTintosAnejados(self, n:int)->bool:
        if n > 0:
            if n > self.__cantTintosAnejados:
                n = self.__cantTintosAnejados
                print(f"Solo se vendieron {n} ya que la cantidad ingresada excede a lo que tenemos")
            self.__cantJugos -= n
            return True
        else: 
            return False

    def obtenerCantidadJugos(self)->int:
        return self.__cantJugos
    
    def obtenerCantidadVinosBlancos(self)->int:
        return self.__cantBlancos
    
    def obtenerCantidadVinosTintosJovenes(self)->int:
        return self.__cantTintosJovenes
    
    def obtenerCantidadVinosTintosAnejados(self)->int:
        return self.__cantTintosAnejados


class testVinoteca:
    @staticmethod
    def test():
        Vinoteca1 = Vinoteca()
        print(Vinoteca1.obtenerCantidadJugos())
        if Vinoteca1.venderJugos(40):
            print(f"Como se vendieron jugos ahora hay {Vinoteca1.obtenerCantidadJugos()}")
        else:
            print("No se vendieron jugos por x razon")
        
        print(Vinoteca1.obtenerCantidadJugos())
        
        if Vinoteca1.venderJugos(6000):
            print(f"Como se vendieron jugos ahora hay {Vinoteca1.obtenerCantidadJugos()}")
        else:
            print("No se vendieron jugos por x razon")
        Vinoteca1.reponerJugos()
        print("Reponemos jugos")
        print(Vinoteca1.obtenerCantidadJugos())  
        print(Vinoteca1.CAPADICAD_MAXIMA)
        
if __name__ == "__main__":
    testVinoteca.test()
    