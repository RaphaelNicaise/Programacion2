from modulo_fecha import Fecha

class Socio:
    def __init__(self, nombre: str, nacimiento: 'Fecha'):
        """
        Inicializa un objeto Socio con nombre y fecha de nacimiento.
        
        :param nombre: Nombre del socio.
        :param nacimiento: Fecha de nacimiento del socio.
        :raises ValueError: Si nacimiento no es una instancia de Fecha.
        """
        if not isinstance(nacimiento, Fecha):
            raise ValueError("Error al ingresar fecha")
        
        self.__nombre = nombre
        self.__fecha_nacimiento = nacimiento
        self.__fecha_penalizacion = None
    
    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Socio.
        
        :return: Cadena con la información del socio.
        """
        msg = f"Socio: {self.__nombre} Nacimiento: {self.__fecha_nacimiento}"
        if self.__fecha_penalizacion is not None:
            msg += f" Penalizado hasta: {self.__fecha_penalizacion}"
        return msg
    
    def establecerNombre(self, nombre: str):
        """
        Establece el nombre del socio.
        
        :param nombre: Nuevo nombre del socio.
        """
        self.__nombre = nombre
    
    def establecerFechaNacimiento(self, fecha: 'Fecha'):
        """
        Establece la fecha de nacimiento del socio.
        
        :param fecha: Nueva fecha de nacimiento del socio.
        :raises ValueError: Si fecha no es una instancia de Fecha.
        """
        if not isinstance(fecha, Fecha):
            raise ValueError("Error al ingresar fecha")
        
        self.__fecha_nacimiento = fecha
    
    def establecerFechaPenalizacion(self, hastaFecha: 'Fecha'):
        """
        Establece la fecha de penalización del socio.
        
        :param hastaFecha: Fecha hasta la cual el socio está penalizado.
        :raises ValueError: Si hastaFecha no es una instancia de Fecha.
        """
        if not isinstance(hastaFecha, Fecha):
            raise ValueError("Error al ingresar fecha")
        
        self.__fecha_penalizacion = hastaFecha
    
    def quitarPenalizacion(self):
        """
        Quita la penalización del socio.
        """
        self.__fecha_penalizacion = None

    def estaHabilitado(self, fecha: 'Fecha') -> bool:
        """
        Verifica si el socio está habilitado en una fecha dada.
        
        :param fecha: Fecha en la que se verifica la habilitación.
        :return: True si el socio está habilitado, False en caso contrario.
        :raises ValueError: Si fecha no es una instancia de Fecha.
        """
        if not isinstance(fecha, Fecha):
            raise ValueError("Error al ingresar fecha")
        
        return self.__fecha_penalizacion is None or self.__fecha_penalizacion.esAnterior(fecha)
    
    def obtenerNombre(self) -> str:
        """
        Obtiene el nombre del socio.
        
        :return: Nombre del socio.
        """
        return self.__nombre
    
    def obtenerFechaNacimiento(self) -> 'Fecha':
        """
        Obtiene la fecha de nacimiento del socio.
        
        :return: Fecha de nacimiento del socio.
        """
        return self.__fecha_nacimiento
    
    def obtenerFechaPenalizacion(self) -> 'Fecha':
        """
        Obtiene la fecha de penalización del socio.
        
        :return: Fecha de penalización del socio.
        """
        return self.__fecha_penalizacion
    
class Libro:
    def __init__(self, nombre: str, autor: str, editorial: str, categoria: chr):
        """
        Inicializa un objeto Libro con nombre, autor, editorial y categoría.
        
        :param nombre: Nombre del libro.
        :param autor: Autor del libro.
        :param editorial: Editorial del libro.
        :param categoria: Categoría del libro.
        """
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria
    
    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Libro.
        
        :return: Cadena con la información del libro.
        """
        return f"Libro: {self.__nombre} de {self.__autor} de la editorial {self.__editorial} de la categoria {self.__categoria}"  
    
    def obtenerNombre(self) -> str:
        """
        Obtiene el nombre del libro.
        
        :return: Nombre del libro.
        """
        return self.__nombre
    
    def obtenerAutor(self) -> str:
        """
        Obtiene el autor del libro.
        
        :return: Autor del libro.
        """
        return self.__autor
    
    def obtenerEditorial(self) -> str:
        """
        Obtiene la editorial del libro.
        
        :return: Editorial del libro.
        """
        return self.__editorial
    
    def obtenerCategoria(self) -> str:
        """
        Obtiene la categoría del libro.
        
        :return: Categoría del libro.
        """
        return self.__categoria
    
class Prestamo:
    def __init__(self, libro: 'Libro', fechaprestamo: 'Fecha', cantDias: int, socio: 'Socio'):
        """
        Inicializa un objeto Prestamo con libro, fecha de préstamo, cantidad de días y socio.
        
        :param libro: Libro prestado.
        :param fechaprestamo: Fecha del préstamo.
        :param cantDias: Cantidad de días del préstamo.
        :param socio: Socio que realiza el préstamo.
        :raises ValueError: Si el socio no está habilitado o si los parámetros no son válidos.
        """
        if not socio.estaHabilitado(fechaprestamo):
            raise ValueError("Socio no habilitado")
        
        if not isinstance(libro, Libro) or not isinstance(fechaprestamo, Fecha) or not isinstance(cantDias, int) or not isinstance(socio, Socio):
            raise ValueError("Error al ingresar parametros")
        
        self.__libro = libro
        self.__fecha_prestamo = fechaprestamo
        self.__fecha_devolucion = fechaprestamo.sumaDias(cantDias)
        self.__socio = socio
        
    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Prestamo.
        
        :return: Cadena con la información del préstamo.
        """
        return f'Prestamo del libro: "{self.__libro.obtenerNombre()}" prestado a {self.__socio.obtenerNombre()} desde {self.__fecha_prestamo} hasta {self.__fecha_devolucion}'
    
    def establecerFechaDevolucion(self, fechadev: 'Fecha'):
        """
        Establece la fecha de devolución del libro y aplica penalización si es necesario.
        
        :param fechadev: Fecha en la que se realizó la devolución del libro.
        :raises ValueError: Si fechadev no es una instancia de Fecha.
        """
        if not isinstance(fechadev, Fecha):
            raise ValueError("Error al ingresar fecha")
        
        if self.__fecha_devolucion.esAnterior(fechadev):
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
            self.__fecha_devolucion = fechadev
    
    def obtenerLibro(self) -> 'Libro':
        """
        Obtiene el libro prestado.
        
        :return: Libro prestado.
        """
        return self.__libro
    
    def obtenerFechaPrestamo(self) -> 'Fecha':
        """
        Obtiene la fecha del préstamo.
        
        :return: Fecha del préstamo.
        """
        return self.__fecha_prestamo
    
    def obtenerFechaDevolucion(self) -> 'Fecha':
        """
        Obtiene la fecha de devolución del préstamo.
        
        :return: Fecha de devolución del préstamo.
        """
        return self.__fecha_devolucion
    
    def estaAtrasado(self, fecha: 'Fecha') -> bool:
        """
        Verifica si el préstamo está atrasado en una fecha dada.
        
        :param fecha: Fecha en la que se verifica el atraso.
        :return: True si el préstamo está atrasado, False en caso contrario.
        :raises ValueError: Si fecha no es una instancia de Fecha.
        """
        if not isinstance(fecha, Fecha):
            raise ValueError("Error al ingresar fecha")
        
        return self.__fecha_devolucion.esAnterior(fecha)
    
    def penalizacion(self) -> 'Fecha':
        pass

class tester:
    @staticmethod
    def test():
        """
        Método de prueba para verificar el funcionamiento de las clases.
        """
        libro_1 = Libro("El principito", "Antonito", "MCEDITORS", 'A')
        print(libro_1)
        socio_1 = Socio("Juan", Fecha(1, 1, 2000))
        socio_1.establecerFechaPenalizacion(Fecha(12, 12, 2020))  # Esta penalizado hasta ese dia
        print(socio_1)
        try:
            prestamo_1_fallido = Prestamo(libro_1, Fecha(1, 1, 2020), 10, socio_1)  # Como esta penalizado no puede sacar el libro
        except ValueError as error:
            print(error)
        
        socio_1.quitarPenalizacion()  # Le sacamos la penalizacion
        
        prestamo_2 = Prestamo(libro_1, Fecha(12, 3, 2020), 10, socio_1)
        prestamo_2.establecerFechaDevolucion(Fecha(25, 3, 2020))  # Devolvemos el libro despues de la fecha de devolucion
        print(prestamo_2)
        print(socio_1)  # Y ahora esta penalizado
        
if __name__ == '__main__':
    tester.test()