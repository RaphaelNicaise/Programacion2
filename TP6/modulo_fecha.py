class Fecha:
    
    DIAS_X_MES = [31,28,31,30,31,30,31,31,30,31,30,31]
                # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11
    def __init__(self,dia:int,mes:int,anio:int):
        
        if not isinstance(dia,int):
            raise ValueError("Error al ingresar dia")
        if not isinstance(mes,int):
            raise ValueError("Error al ingresar mes")
        if not isinstance(anio,int):
            raise ValueError("Error al ingresar anio")
        
        if mes > 12 or mes < 0:
            raise ValueError("Los meses tiene que estar entre 1 y 12")
        
        if dia < 0 or dia > Fecha.DIAS_X_MES[mes-1] :
            raise ValueError("Los dias no estan en el rango de dias que permite el mes")
        
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        
    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__anio}"
    
    # Comandos
    
    def establecerDia(self,dia:int):
        if not isinstance(dia,int):
            print("No es un dato de tipo correcto")
            return None
        
        if dia > 0 and dia <= Fecha.DIAS_X_MES[self.__mes-1]:
            self.__dia = dia
        else:
            print("Error al establecer dia")
            
    def establecerMes(self,mes:int):
        if not isinstance(mes,int):
            print("No es un dato de tipo correcto")
            return None
        
        if mes <= 12 and mes > 0:
            
            if self.__dia > Fecha.DIAS_X_MES[mes-1]:
                # Si el dia es mayor al limite de dias de el mes a cambiar, los dias se cambian al limite del mes asignado
                # Si mes 3 y fecha 31, cambio a mes 2, y automaticamente se cambia a 28 (fecha limite febrero)
                self.__dia = Fecha.DIAS_X_MES[mes-1]
            
            self.__mes = mes
        else:
            print("Error al establecer mes")
    
    def establecerAnio(self,anio:int):
        if not isinstance(anio,int):
            print("No es un dato de tipo correcto")
            return None

        self.__anio = anio
    # Consultas
    
    def obtenerDia(self)->int:
        return self.__dia
    
    def obtenerMes(self)->int:
        return self.__mes
    
    def obtenerAnio(self)->int:
        return self.__anio
    
    def esAnterior(self,otraFecha:'Fecha')->bool:
        """
        retorna verdadero si la fecha que recibe el mensaje es anterior a 
        la fecha pasada por parámetro, y falso en caso contrario
        Args:
            otraFecha (Fecha): _description_
        Returns:
            bool: _description_
        """
        if self.esIgualQue(otraFecha):
           print("Son iguales")
           return False        
        # of (30/4/23) sa (31/5/21)
        if otraFecha.obtenerAnio() < self.__anio:
            return False
        elif otraFecha.obtenerAnio() > self.__anio:
            return True
        
        if otraFecha.obtenerMes() < self.__mes:
            return False
        elif otraFecha.obtenerMes() > self.__mes:
            return True

        if otraFecha.obtenerDia() < self.__dia:
            return False
        elif otraFecha.obtenerDia() > self.__dia:
            return True
        
    def sumaDias(self,cantDias:int)->'Fecha':
        """
        retorna la fecha que resulta de sumar la cantidad de días recibida 
        por parámetro a la fecha que recibe el mensaje 
        Args:
            cantDias (int): _description_
        Returns:
            Fecha: _description_
        """
        if not cantDias > 0:
            return None
        
        dia = self.__dia
        mes = self.__mes
        anio = self.__anio
        
        for _ in range(cantDias):
            if dia + 1 > Fecha.DIAS_X_MES[mes-1]:
                if mes == 12:
                    mes = 1
                    anio += 1   
                else:    
                    mes += 1
                
                dia = 1
            else:
                dia += 1
        
        return Fecha(dia,mes,anio)
    
    def diaSiguiente(self)->'Fecha':
        """
        retorna una nueva fecha con los valores del día siguiente a la fecha que recibe el mensaje  
        Returns:
            Fecha: _description_
        """
        # Si nos pasamos de dias del mes, cambiamos mes, y si nos pasamos de mes, sumamos anio
        
        if self.__dia + 1 > Fecha.DIAS_X_MES[self.__mes-1]:
            
            if self.__mes == 12:
                
                mes = 1
                anio = self.__anio + 1   
            else:    
                
                mes = self.__mes + 1
                anio = self.__anio
            
            dia = 1

        else:
            anio = self.__anio
            mes = self.__mes
            dia = self.__dia+1
             
        
        return Fecha(dia,mes,anio)
         
    
    def esIgualQue(self,otraFecha:'Fecha')->bool:
        """
        retorna true si otraFecha es equivalente a la fecha que recibe el mensaje 
        Args:
            otraFecha (Fecha): _description_

        Returns:
            bool: _description_
        """
        if not self.__dia == otraFecha.obtenerDia():
            return False
        if not self.__mes == otraFecha.obtenerMes():
            return False
        if not self.__anio == otraFecha.obtenerMes():
            return False
        
        return True
    
    def esBisiesto(self)->bool:
        return self.__anio % 4 == 0 and (self.__anio % 100 != 0 or self.__anio % 400 == 0)
    
    @staticmethod
    def ingresar_fecha():
        dia = int(input("Ingrese dia: "))
        mes = int(input("Ingrese mes: "))
        anio = int(input("Ingrese anio: "))
    
        return Fecha(dia,mes,anio)
    
    
class tester:
    @staticmethod
    def test():
        try:
            fecha1 = Fecha(31,2,2022) # 31 de Febrero no existe
            print(fecha1)
        except ValueError as e:
            print(e)
         
        fecha2 = Fecha(30,7,2021)  
        print(fecha2)
        fecha2.establecerDia(31) # Abril dura 30 dias
        print(fecha2)
        
        fecha2.establecerMes(2) # Esto cambia al mes 2, y pone la fecha como el limite del mes 2 (28)
        print(fecha2)
        
        fecha3 = Fecha(23,7,2021)
        fecha4 = Fecha(31,7,2021)
        if fecha3.esAnterior(fecha4):
            print("Fecha3 es anterior a fecha4")
        else:
            print("Fecha3 no es anterior a fecha4")
        
        # Dia siguiente de la fecha 4
        fecha5 = fecha4.diaSiguiente()
        print("fecha5 siguiente a la fecha4",fecha5)
            
        fecha6 = fecha4.sumaDias(4)    
        print("fecha 6",fecha6)


                    
if __name__ == "__main__":
    tester.test()