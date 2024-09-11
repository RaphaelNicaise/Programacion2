class Empleado:
    def __init__(self,legajo:int, cantHoras:int=0, valorHora:float=0):
        """_summary_

        Args:
            legajo (int): _description_
            cantHoras (int, optional): _description_. Defaults to 0.
            valorHora (float, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            TypeError: _description_
            TypeError: _description_
        """
        if legajo < 0:
            raise TypeError("El valor del legajo es incorrecto")
        if not isinstance(cantHoras,int) or cantHoras < 0:
            raise TypeError("La cantidad de horas debe ser entera y mayor a 0")
        if not isinstance(valorHora,(int, float)) or valorHora < 0:
            raise TypeError("El valor de hora no es correcto")
        
        self.__legajo = legajo
        self.__cantHoras = cantHoras
        self.__valorHora = valorHora
    
    def establecerHorasTrabajadas(self, horas:int)->bool:
        """_summary_
        Args:
            horas (int): _description_
        Returns:
            bool: _description_
        """

        
        if horas > -1:
            self.__cantHoras = horas
            return True
        else:
            return False
    
    def establecerValorHora(self, valor:float)->bool:
        """_summary_
        Args:
            valor (float): _description_

        Returns:
            bool: _description_
        """
        if valor > -1:
            self.__valorHora = valor
            return True
        else:
            return False
        
    def obtenerLegajo(self)->int:
        return self.__legajo
    
    def obtenerHorasTrabajadas(self)->int:
        return self.__cantHoras
    
    def obtenerValorHora(self)->float:
        return self.__valorHora
    
    def obtenerSueldo(self)->float:
        return self.__cantHoras * self.__valorHora
    
    
        
class TestEmpleado:
        @staticmethod
        def test():
            emp1 = Empleado(111,25,2000)
            emp2 = Empleado(222)
            print(f"Sueldo emp1 {emp1.obtenerSueldo()}$")
            print(f"Sueldo emp2 {emp2.obtenerSueldo()}$")

            if emp2.establecerHorasTrabajadas(30):
                print("El emp2 ahora trabajo 30 horas")
            else:
                print("Error al establecer horas del emp2")
                
            if emp2.establecerHorasTrabajadas(-5):
                print("El emp2 ahora trabajo 30 horas")
            else:
                print("Error al establecer horas del emp2")
            
            print(f"Emp2 Trabajo {emp2.obtenerHorasTrabajadas()} horas")
            print(f"Emp2 valor hora: {emp2.obtenerValorHora()}")        
            
            if emp2.establecerValorHora(3000):
                print(f"Actualizacion Emp2 valor hora: {emp2.obtenerValorHora()}")            
            else:
                print("Error al establecer valor de hora")

            if emp2.establecerValorHora(-5000):
                print(f"Actualizacion Emp2 valor hora: {emp2.obtenerValorHora()}")            
            else:
                print("Error al establecer valor de hora")
                
            print("Sueldo de emp2 ahora ",emp2.obtenerSueldo()," $")    

if __name__ == "__main__":  
    TestEmpleado.test()