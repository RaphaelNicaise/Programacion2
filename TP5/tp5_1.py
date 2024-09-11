class Atleta:
    MAX_VALOR=100
    MIN_VALOR=1
    
    def __init__(self,nombre:str) -> None:
        
        if not isinstance(nombre,str):
            raise ValueError("El nombre debe ser un string")
        
        self.__nombre = nombre
        self.__energia = Atleta.MAX_VALOR
        self.__destreza = Atleta.MIN_VALOR
        self.__cantEntrenamientos = 0
    
    def __str__(self) -> str:
        return f"Atleta: {self.__nombre} Energia: {self.__energia} Destreza: {self.__destreza}"
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_energia(self):
        return self.__energia
    
    def obtener_destreza(self):
        return self.__destreza
    
    def establecer_energia(self,n:int):
        if not isinstance(n,int) or n > Atleta.MAX_VALOR or n < Atleta.MIN_VALOR:
            print("Error al ingresar energia")
            return
        self.__energia = n
        
    def establecer_destreza(self,n:int):
        if not isinstance(n,int) or  n > Atleta.MAX_VALOR or n < Atleta.MIN_VALOR:
            print("Error al ingresar destreza")
            return 
        self.__destreza = n
        
    def entrenar(self)->bool:
        if self.__energia <= 5:
            print(f"{self.__nombre} no tiene energia suficiente para entrenar")
            return False
        
        print(f"{self.__nombre} entrena")
        if self.__energia - 5 > Atleta.MIN_VALOR:
            self.__energia -= 5
        else:
            self.__energia = Atleta.MIN_VALOR
        
        self.__cantEntrenamientos += 1
        
        if self.__cantEntrenamientos >= 5: 
            self.__destreza += 1
            self.__cantEntrenamientos = 0
        
        return True
    
    def descansar(self):
        print(f"{self.__nombre} descansa")
        if self.__energia + 20 < Atleta.MAX_VALOR:
            self.__energia += 20
        else:
            self.__energia = Atleta.MAX_VALOR

    def mismaDestrezaQue(self,otroAtleta:'Atleta')->bool:
        return otroAtleta.obtener_destreza() == self.__destreza
    
    def mayorDestrezaQue(self,otroAtleta:'Atleta')->bool:
        return self.__destreza > otroAtleta.obtener_destreza()
    
class testAtletas:
    @staticmethod
    def test():
        
        atleta1 = Atleta("Miguel")
        print(atleta1)
        for _ in range(20):
         atleta1.entrenar()
         print(atleta1)
         
        for _ in range(3):
            atleta1.descansar()
            print(atleta1)
            
        atleta1.establecer_energia("hola")
        atleta1.establecer_destreza(30)
        print(atleta1)
        
        atleta2 = Atleta("Juan")
        
        if atleta1.mayorDestrezaQue(atleta2):
            print(f"{atleta1.obtener_nombre()} tiene mayor destreza que {atleta2.obtener_nombre()}")
        else:
            print(f"{atleta1.obtener_nombre()} no tiene mayor destreza que {atleta2.obtener_nombre()}")
            
        if atleta1.mismaDestrezaQue(atleta2):
            print(f"{atleta1.obtener_nombre()} tiene la misma destreza que {atleta2.obtener_nombre()}")
        else:
            print(f"{atleta1.obtener_nombre()} no tiene la misma destreza que {atleta2.obtener_nombre()}")
            
if __name__ == '__main__':
    testAtletas.test()
        