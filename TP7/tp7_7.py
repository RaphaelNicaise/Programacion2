from abc import ABC,abstractmethod
from fecha import Fecha

class Empleado(ABC):
    def __init__(self,dni:str,nombre:str,apellido:str,fechaIngreso:'Fecha'):
        if not isinstance(dni,str) or not isinstance(nombre,str) or not isinstance(apellido,str) or not isinstance(fechaIngreso,Fecha):
            raise ValueError("Error al ingresar los datos del empleado")
        
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._fechaIngreso = fechaIngreso
    
    @abstractmethod
    def __str__(self):
        pass
    
    # Comandos
    
    def setNombre(self,nombreNuevo):
        if not isinstance(nombreNuevo,str):
            raise ValueError("Error al ingresar el nombre")
        self._nombre = nombreNuevo
        
    def setApellido(self,apellidoNuevo):
        if not isinstance(apellidoNuevo,str):
            raise ValueError("Error al ingresar el apellido")
        self._apellido = apellidoNuevo
    
    def setFechaIngreso(self,fechaIngresoNueva):
        if not isinstance(fechaIngresoNueva,Fecha):
            raise ValueError("Error al ingresar la fecha de ingreso")
        self._fechaIngreso = fechaIngresoNueva
        
    # Consultas
    
    def getDni(self):
        return self._dni
    
    def getNombre(self):
        return self._nombre
    
    def getApellido(self):
        return self._apellido
    
    def getFechaIngreso(self):
        return self._fechaIngreso
    
    @abstractmethod
    def getSalario(self):
        pass
    
    def __eq__(self,otroEmpleado):
        return self._dni == otroEmpleado.getDni()
    
class EmpleadoAComision(Empleado):
    
    __EMPLEADOS_A_COMISION: list['EmpleadoAComision'] = []
    
    def __init__(self,dni:str,nombre:str,apellido:str,fechaIngreso:'Fecha',salarioMinimo:float,clientesCaptados:int,montoPorCliente:float):
        if not isinstance(float(salarioMinimo),float) or salarioMinimo < 0:
            raise ValueError("Error al ingresar el salario minimo")
        if not isinstance(clientesCaptados,int) or clientesCaptados < 0:
            raise ValueError("Error al ingresar la cantidad de clientes captados")
        if not isinstance(float(montoPorCliente),float) or montoPorCliente < 0:
            raise ValueError("Error al ingresar el monto por cliente")
        
        super().__init__(dni,nombre,apellido,fechaIngreso)
        
        self.__salarioMinimo = salarioMinimo
        self.__clientesCaptados = clientesCaptados
        self.__montoPorCliente = montoPorCliente
        self.__EMPLEADOS_A_COMISION.append(self)
        
    def __str__(self):
        return f"Empleado a comision: {self._nombre} {self._apellido} {self._dni} Ingreso:{self._fechaIngreso} Salario Minimo:{self.__salarioMinimo} Clientes:{self.__clientesCaptados} Monto por Cliente:{self.__montoPorCliente}"
    
    def __repr__(self):
        return f"{self._dni}"
    # Comandos
    def setSalarioMinimo(self,salarioMNuevo):
       if not isinstance(float(salarioMNuevo),float) or salarioMNuevo < 0:
            raise ValueError("Error al ingresar el salario minimo")
       self.__salarioMinimo = salarioMNuevo
       
    def setClientesCaptados(self,clientesCaptadosNuevos):
        if not isinstance(clientesCaptadosNuevos,int) or clientesCaptadosNuevos < 0:
            raise ValueError("Error al ingresar la cantidad de clientes captados")
        self.__clientesCaptados = clientesCaptadosNuevos
        
    def setMontoPorCliente(self,montoPorClienteNuevo):
        if not isinstance(float(montoPorClienteNuevo),float) or montoPorClienteNuevo < 0:
            raise ValueError("Error al ingresar el monto por cliente")
        self.__montoPorCliente = montoPorClienteNuevo
        
    def quitarEmpleado(self):
        self.__EMPLEADOS_A_COMISION.remove(self)
    
    # Consultas
    
    def getSalarioMinimo(self):
        return self.__salarioMinimo
    
    def getClientesCaptados(self):
        return self.__clientesCaptados
    
    def getMontoPorCliente(self):
        return self.__montoPorCliente
    
    def getSalario(self):
        monto_x_clientes = self.__clientesCaptados * self.__montoPorCliente
        if monto_x_clientes < self.__salarioMinimo:
            return self.__salarioMinimo
        return monto_x_clientes
    
    @staticmethod
    def getEmpleadosAComision():
        return EmpleadoAComision.__EMPLEADOS_A_COMISION
    
class EmpleadoSalarioFijo(Empleado):
    def __init__(self,dni:str,nombre:str,apellido:str,fechaIngreso:'Fecha',salarioFijo:float):
        if not isinstance(float(salarioFijo),float) or salarioFijo < 0:
            raise ValueError("Error al ingresar el salario fijo")
        super().__init__(dni,nombre,apellido,fechaIngreso)
        
        self.__salarioFijo = salarioFijo
        
    def __str__(self):
        return f"Empleado salario fijo: {self._nombre} {self._apellido} {self._dni} Ingreso:{self._fechaIngreso} Salario Fijo:{self.__salarioFijo}"
    
    # Comandos
    
    def setSalarioFijo(self,salarioFijoNuevo):
        if not isinstance(float(salarioFijoNuevo),float) or salarioFijoNuevo < 0:
            raise ValueError("Error al ingresar el salario fijo")
        self.__salarioFijo = salarioFijoNuevo
    
    # Consultas
    
    def getSalarioFijo(self):
        return self.__salarioFijo
    
    def getSalario(self):
        
        hoy = Fecha.obtenerFechaActual()
        dias = hoy.diasDiferencia(self.getFechaIngreso())
        años = dias // 365
        
        if años < 2:
            return self.__salarioFijo
        elif 2 <= años <= 5:
            return self.__salarioFijo + self.__salarioFijo*0.05
        else:
            return self.__salarioFijo + self.__salarioFijo*0.10
        
class Tester:
    @staticmethod
    def run():
        try:
            Empleado("5022435","Raphael","Gonzalez",Fecha(12,12,2020))
        except TypeError as e:
            print(f"Error: {e}")
        
        empleado_1 = EmpleadoAComision("3485963","Hernan","Gonzalez",Fecha(12,12,2020),20000,21,1000)
        print(empleado_1)
        print(empleado_1.getSalario())
        empleado_2 = EmpleadoSalarioFijo("6432346","Nicolas","Hernandez",Fecha(12,12,2028),15000)
        print(empleado_2.getSalario())
        print(EmpleadoAComision.getEmpleadosAComision())
        empleado_1.quitarEmpleado()
        print(EmpleadoAComision.getEmpleadosAComision())
        
if __name__ == "__main__":
    Tester.run()