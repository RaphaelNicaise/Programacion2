class MascotaVirtual:
    MAX = 100
    MIN = 0
    
    def __init__(self,nombre:str):
        """_summary_
        Args:
            nombre (str): _description_
        """
        self.__nombre = nombre
        self.__energia = MascotaVirtual.MAX
        self.__diversion = MascotaVirtual.MAX
        self.__higiene = MascotaVirtual.MAX
        self.__dormido = False
        self.__cantActividadesDesgaste = 0
    
    def __str__(self):
        """_summary_
        Returns:
            _type_: _description_
        """
        return f"Nombre: {self.__nombre}\nEnergia: {self.__energia}\nDiversion: {self.__diversion}\nHigiene: {self.__higiene}\nDormido: {self.__dormido}"
    # Comandos
    def dormir(self):
        """_summary_
        """
        if self.estaVivo():
            if self.__dormido:
                print("Ya esta durmiendo")
            else:
                self.__dormido = True
                print(f"El {self.__nombre} se Durmio")
            self.__cantActividadesDesgaste = 0

    def despertar(self):
        if self.estaVivo():
            if self.__dormido:
                self.__dormido = False
                print(f"El {self.__nombre} Desperto")
            else:
                print("Ya esta despierto")
    
    def comer(self):
        """_summary_
        """
        if self.estaVivo():
            if not self.__dormido:
                if self.__energia + 20 < MascotaVirtual.MAX:
                    self.__energia += 20 
                else:
                    self.__energia = MascotaVirtual.MAX
                
                print(f"El {self.__nombre} Comio")
                self.__cantActividadesDesgaste = 0
            else:
                print("No puede comer si esta dormido")
    def beber(self):
        """_summary_
        """
        if self.estaVivo():
            if not self.__dormido:        
                if self.__energia + 10 < MascotaVirtual.MAX:
                    self.__energia += 10 
                else:
                    self.__energia = MascotaVirtual.MAX

                print(f"{self.__nombre} Bebio")
                self.__cantActividadesDesgaste = 0
            else:
                print("No puede beber si esta dormido")
                
                
    def baniar(self):
        """_summary_
        """
        if self.estaVivo():
            if not self.__dormido:    
                if self.__diversion - 10 > MascotaVirtual.MIN:
                    self.__diversion -= 10
                else:
                    self.__diversion = MascotaVirtual.MIN

                if self.__higiene + 40 < MascotaVirtual.MAX:
                    self.__higiene += 40
                else:
                    self.__higiene = MascotaVirtual.MAX

                self.__cantActividadesDesgaste = 0    
                print(f"El {self.__nombre} se baño")
            else:
                print("No puede bañarse si esta dormido")    
        
    def jugar(self)->bool:
        """_summary_
        Returns:
            _type_: _description_
        """
        if self.estaVivo():
                
            if not self.__dormido:
                if self.__diversion + 40 < MascotaVirtual.MAX:
                    self.__diversion += 40
                else:
                    self.__diversion = MascotaVirtual.MAX

                if self.__energia - 20 > MascotaVirtual.MIN:    
                    self.__energia -= 20
                else:
                    self.__energia = MascotaVirtual.MIN   

                if self.__higiene - 15 > MascotaVirtual.MIN:
                    self.__higiene -= 15
                else:
                    self.__higiene = MascotaVirtual.MIN

                self.__cantActividadesDesgaste += 1
                print(f"El {self.__nombre} Jugó")
                
                if self.__cantActividadesDesgaste >= 3:
                    self.dormir()
                
                return True
            else:
                print("No puede jugar si esta dormido")
                return False
        return False
    def caminar(self)->bool:
        """_summary_
        """
        if self.estaVivo():
            
            if not self.__dormido:        
                if self.__diversion + 20 < MascotaVirtual.MAX:
                    self.__diversion += 20
                else:
                    self.__diversion = MascotaVirtual.MAX

                if self.__energia - 10 > MascotaVirtual.MIN:    
                    self.__energia -= 10
                else:
                    self.__energia = MascotaVirtual.MIN
                    
                if self.__higiene - 8 > MascotaVirtual.MIN:
                    self.__higiene -= 8
                else:
                    self.__higiene = MascotaVirtual.MIN
                
                self.__cantActividadesDesgaste += 1
                print(f"El {self.__nombre} Caminó")
                
                if self.__cantActividadesDesgaste >= 3:
                    self.dormir()
                return True
            else:
                print("No puede caminar si esta dormido")
                return False
        return False    
    def saltar(self)->bool:
        """_summary_
        """
        if self.estaVivo():
                
            if not self.__dormido:        
                if self.__diversion + 10 < MascotaVirtual.MAX:
                    self.__diversion += 10
                else:
                    self.__diversion = MascotaVirtual.MAX

                if self.__energia - 15 > MascotaVirtual.MIN:    
                    self.__energia -= 15
                else:
                    self.__energia = MascotaVirtual.MIN

                if self.__higiene - 5 > MascotaVirtual.MIN:
                    self.__higiene -= 5
                else:
                    self.__higiene = MascotaVirtual.MIN
                    
                self.__cantActividadesDesgaste += 1
                print(f"El {self.__nombre} Salto")
                
                if self.__cantActividadesDesgaste >= 3:
                    self.dormir()
                return True
            else:
                print("No puede saltar si esta dormido")
                return False
            
        return False
    # Consultas
    
    def obtenerNombre(self)->str:
        """_summary_
        Returns:
            str: _description_
        """
        return self.__nombre
    
    def obtenerEnergia(self)->int:
        return self.__energia
    
    def obtenerDiversion(self)->int:
        return self.__diversion
    
    def obtenerHigiene(self)->int:
        return self.__higiene
    
    def estaDormido(self)->bool:
        return self.__dormido
    
    def obtenerHumor(self)->str:
        energia=self.__energia 
        diversion=self.__diversion
        higiene=self.__higiene
        
        if energia>=70 and diversion>=70 and higiene>=70:
            return "Humor feliz"
        elif (50<=energia<70 and 50<=diversion<70)or(50<=energia<70 and 50<=higiene<70)or(50<=diversion<70 and 50<=higiene<70):
            return "Humor Alegre"
        elif (30<=energia<50 and 30<=diversion<50)or(30<=energia<50 and 30<=higiene<50)or(30<=diversion<50 and 30<=higiene<50):
            return "Humor Neutral"
        elif (10<=energia<30 and 10<=diversion<30)or(10<=energia<30 and 10<=higiene<30)or(10<=diversion<30 and 10<=higiene<30):
            return "Humor Triste"
        else:
            return "Humor Muy Triste"
    
    def estaVivo(self)->bool:
        if self.__energia == MascotaVirtual.MIN:
            print(f"El {self.__nombre} esta muerto. RIP")
            return False
        else:
            return True
    
class TestMascotaVirtual:
    @staticmethod
    def test():
        Tamagotchi = MascotaVirtual("Tamagotchi")    
        Tamagotchi.jugar()
        Tamagotchi.jugar()
        Tamagotchi.jugar()
        print(Tamagotchi)
        Tamagotchi.jugar()        
    
if __name__ == "__main__":
    TestMascotaVirtual.test()