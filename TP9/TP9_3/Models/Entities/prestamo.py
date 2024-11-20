import datetime

class Prestamo:
    
    ULTIMO_ID = 0
    
    def __init__(self,socio_dni:int, libro_isbn:str, fecha_retiro:str,cant_dias:int, fecha_devolucion:str = None, id = None):
        if not isinstance(socio_dni,int):
            raise ValueError("El dni debe ser un entero")
        if not isinstance(libro_isbn,str) or libro_isbn in [""," ",None]:
            raise ValueError("El isbn debe ser un string")
        if not isinstance(fecha_retiro,str):
            raise ValueError("La fecha de retiro debe ser un string")
        if fecha_devolucion != None and not isinstance(fecha_devolucion,str):
            raise ValueError("La fecha de devolucion debe ser un string")
        if not isinstance(cant_dias,int):
            raise ValueError("La cantidad de dias debe ser un entero")
        
        # Para las fechas, verificar que tengan este formato 'YYYY-MM-DD'
        
        if Prestamo.verificar_formato_fecha(fecha_retiro) == False:
            raise ValueError("La fecha de retiro debe tener el formato 'YYYY-MM-DD'")
        
        if fecha_devolucion != None and Prestamo.verificar_formato_fecha(fecha_devolucion) == False:
            raise ValueError("La fecha de devolucion debe tener el formato 'YYYY-MM-DD'")
    
        
        self.__socio_dni = socio_dni
        self.__libro_isbn = libro_isbn
        self.__fecha_retiro = fecha_retiro
        self.__cant_dias = cant_dias
        self.__fecha_devolucion = fecha_devolucion if fecha_devolucion != None else None
        self.__id = id if id != None else Prestamo.obtenerNuevoId()
    
    def __str__(self):
        return f'{self.__socio_dni} - {self.__libro_isbn} - {self.__fecha_retiro} - {self.__cant_dias} - {self.__fecha_devolucion} - {self.__id}' 
    
    def __eq__(self, otroPrestamo: 'Prestamo'):
        return self.getId() == otroPrestamo.getId()
    
    @classmethod
    def fromDict(cls, dict):
        return cls(dict['socio_dni'], dict['libro_isbn'], dict['fecha_retiro'],dict['cant_dias'], dict['fecha_devolucion'], dict['id'])
    
    def toDict(self):
        return {
            'socio_dni': self.__socio_dni,
            'libro_isbn': self.__libro_isbn,
            'fecha_retiro': self.__fecha_retiro,
            'cant_dias': self.__cant_dias,
            'fecha_devolucion': self.__fecha_devolucion,
            'id': self.__id
        }
        
    # Getters
    
    def getSocioDni(self):
        return self.__socio_dni
    
    def getLibroIsbn(self):
        return self.__libro_isbn
    
    def getFechaRetiro(self):
        return self.__fecha_retiro
    
    def getCantDias(self):
        return self.__cant_dias
    
    def getFechaDevolucion(self):
        return self.__fecha_devolucion
    
    def getId(self):
        return self.__id
    
    # Setters
    
    def setSocioDni(self, socio_dni):
        if not isinstance(socio_dni,int):
            raise ValueError("El dni debe ser un entero")
        self.__socio_dni = socio_dni
        
    def setLibroIsbn(self, libro_isbn):
        if not isinstance(libro_isbn,str) or libro_isbn in [""," ",None]:
            raise ValueError("El isbn debe ser un string")
        self.__libro_isbn = libro_isbn
        
    def setFechaRetiro(self, fecha_retiro):
        if not isinstance(fecha_retiro,str):
            raise ValueError("La fecha de retiro debe ser un string")
        if Prestamo.verificar_formato_fecha(fecha_retiro) == False:
            raise ValueError("La fecha de retiro debe tener el formato 'YYYY-MM-DD'")
        self.__fecha_retiro = fecha_retiro
        
    def setCantDias(self, cant_dias):
        if not isinstance(cant_dias,int):
            raise ValueError("La cantidad de dias debe ser un entero")
        self.__cant_dias = cant_dias
        
    def setFechaDevolucion(self, fecha_devolucion):
        if fecha_devolucion != None and not isinstance(fecha_devolucion,str):
            raise ValueError("La fecha de devolucion debe ser un string")
        if Prestamo.verificar_formato_fecha(fecha_devolucion) == False:
            raise ValueError("La fecha de devolucion debe tener el formato 'YYYY-MM-DD'")
        
        self.__fecha_devolucion = fecha_devolucion
    
    @staticmethod
    def verificar_formato_fecha(fecha):
        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    @classmethod
    def obtenerNuevoId(cls):
        """Obtiene un nuevo id para un prestamo,
        y suma 1 a la variable de clase ULTIMO_ID.

        Returns:
            int: Nuevo id
        """
        cls.ULTIMO_ID += 1
        return cls.ULTIMO_ID
    
    @classmethod
    def establecerUltimoId(cls, id):
        cls.ULTIMO_ID = id
        
