from modulo_fecha import Fecha

class Socio:
    def __init__(self,nombre:str,nacimiento:'Fecha'):
        self.__nombre = nombre
        self.__fecha_nacimiento = nacimiento
        self.__fecha_penalizacion = None
    
    def __str__(self):
        msg = f"Socio: {self.__nombre} Nacimiento: {self.__fecha_nacimiento}"
        if self.__fecha_penalizacion != None:
            msg += f" Penalizado hasta: {self.__fecha_penalizacion}"
        return msg
    
    # Comandos
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
    
    def establecerFechaNacimiento(self,fecha:'Fecha'):
        if not isinstance(fecha,Fecha):
            raise ValueError("Error al ingresar fecha")
        self.__fecha_nacimiento = fecha
    
    def establecerFechaPenalizacion(self,hastaFecha:'Fecha'):
        if not isinstance(hastaFecha,Fecha):
            raise ValueError("Error al ingresar fecha")
        self.__fecha_penalizacion = hastaFecha
    
    def quitarPenalizacion(self):
        self.__fecha_penalizacion = None

    # Consultas
    def estaHabilitado(self,fecha:'Fecha')->bool:
        return self.__fecha_penalizacion == None or self.__fecha_penalizacion.esAnterior(fecha)
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self)->'Fecha':
        return self.__fecha_nacimiento
    
    def obtenerFechaPenalizacion(self)->'Fecha':
        return self.__fecha_penalizacion
    
            
class Libro:
    def __init__(self,nombre:str,autor:str,editorial:str,categoria:chr):
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria
    
    def __str__(self):
        return f"Libro: {self.__nombre} de {self.__autor} de la editorial {self.__editorial} de la categoria {self.__categoria}"  
    
    # Consultas
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerAutor(self)->str:
        return self.__autor
    
    def obtenerEditorial(self)->str:
        return self.__editorial
    
    def obtenerCategoria(self)->str:
        return self.__categoria
    
    
class Prestamo:
    def __init__(self,libro:'Libro',fechaprestamo:'Fecha',cantDias:int,socio:'Socio'):
        
        if not socio.estaHabilitado(fechaprestamo):
            raise ValueError("Socio no habilitado")
        
        self.__libro = libro
        self.__fecha_prestamo = fechaprestamo
        self.__fecha_devolucion = fechaprestamo.sumaDias(cantDias)
        self.__socio = socio
        
    def __str__(self):
        return f'Prestamo del libro: "{self.__libro.obtenerNombre()}" prestado a {self.__socio.obtenerNombre()} desde {self.__fecha_prestamo} hasta {self.__fecha_devolucion}'
    
    # Comandos
    
    def establecerFechaDevolucion(self,fechadev:'Fecha'):
        """
        establecerFechaDevolucion recibe como parámetro la fecha en la que 
        efectivamente se realizó la devolución del libro, y controla si el socio debe 
        recibir una penalización, en caso afirmativo se le asigna al socio la fecha de 
        penalización.
        """
        if not isinstance(fechadev,Fecha):
            raise ValueError("Error al ingresar fecha")
        
        if self.__fecha_devolucion.esAnterior(fechadev):
            # Si la fecha de devolucion preevista es anterior a la fecha de devolucion real
            dias_diferencia = 0
            
            while self.__fecha_devolucion.esAnterior(fechadev):
                self.__fecha_devolucion = self.__fecha_devolucion.diaSiguiente()
                dias_diferencia += 1
            
            if dias_diferencia < 7:
                dias_penalizacion = 3
            elif 7 <= dias_diferencia < 21:
                dias_penalizacion = 5
            elif dias_diferencia >= 21:
                dias_penalizacion = 10
                
            if self.__libro.obtenerCategoria() == 'A':
                dias_penalizacion *= 2
                
            self.__socio.establecerFechaPenalizacion(fechadev.sumaDias(dias_penalizacion))   
        else:
            # si lo devolvemos antes de la fecha establecida
            self.__fecha_devolucion = fechadev
    
            
        
    # Consultas
    
    def obtenerLibro(self)->'Libro':
        return self.__libro
    
    def obtenerFechaPrestamo(self)->'Fecha':
        return self.__fecha_prestamo
    
    def obtenerFechaDevolucion(self)->'Fecha':
        return self.__fecha_devolucion
    
    def estaAtrasado(self,fecha:'Fecha')->bool:
        return self.__fecha_devolucion.esAnterior(fecha)
    
    def penalizacion(self)->'Fecha':
        """penalizacion calcula la cantidad de días de penalización y devuelve la fecha 
hasta la que corresponde aplicar la penalización, a partir de la fecha de 
devolución, que tiene que estar ligada. La penalización es de 3 días si se 
atrasó menos de una semana, 5 días si se atrasó menos de tres semanas y 
10 días si se atrasó 3 semanas o más. Si el libro tiene categoría A los días de 
penalización se duplican"""
        # Ya aplicado en funcion establecerFechaDevolucion
        pass

    
class tester:
    @staticmethod
    def test():
        libro_1 = Libro("El principito","Antonito","MCEDITORS",'A')
        print(libro_1)
        socio_1 = Socio("Juan",Fecha(1,1,2000))
        socio_1.establecerFechaPenalizacion(Fecha(12,12,2020)) # Esta penalizado hasta ese dia
        print(socio_1)
        try:
            prestamo_1_fallido = Prestamo(libro_1,Fecha(1,1,2020),10,socio_1) # Como esta penalizado no puede sacar el libro
        except ValueError as error:
            print(error)
        
        socio_1.quitarPenalizacion() # Le sacamos la penalizacion
        
        prestamo_2 = Prestamo(libro_1,Fecha(12,3,2020),10,socio_1)
        prestamo_2.establecerFechaDevolucion(Fecha(25,3,2020)) # Devolvemos el libro despues de la fecha de devolucion
        print(prestamo_2)
        print(socio_1) # Y ahora esta penalizado
        
if __name__ == '__main__':
    tester.test()