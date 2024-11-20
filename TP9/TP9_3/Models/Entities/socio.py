
class Socio:
    def __init__(self,dni:int,nombre:str,apellido:str,mail:str,fecha_nacimiento:str):
        if not isinstance(dni,int):
            raise ValueError("El dni debe ser un entero")
        if not isinstance(nombre,str) or nombre in [""," ",None]:
            raise ValueError("El nombre debe ser un string")
        if not isinstance(apellido,str) or apellido in [""," ",None]:
            raise ValueError("El apellido debe ser un string")
        if not isinstance(mail,str) or mail in [""," ",None]:
            raise ValueError("El mail debe ser un string")
        
        if not isinstance(fecha_nacimiento,str):
            raise ValueError("La fecha de nacimiento debe ser un datetime.date")
        
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__fecha_nacimiento = fecha_nacimiento
    
    def __str__(self):
        return f"{self.__nombre} {self.__apellido} ({self.__dni}) - {self.__mail} - {self.__fecha_nacimiento}"
    
    def toDict(self):
        return {
            'dni': self.__dni,
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'mail': self.__mail,
            'fecha_nacimiento': self.__fecha_nacimiento
        }
        
    @classmethod
    def fromDict(cls, dict):
        return cls(
            dict['dni'],
            dict['nombre'],
            dict['apellido'],
            dict['mail'],
            dict['fecha_nacimiento']
        )
    
    # Getters
    
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getMail(self):
        return self.__mail
    
    def getFechaNacimiento(self):
        return self.__fecha_nacimiento
    
    # Setters
    
    def setDni(self,dni:int):
        if not isinstance(dni,int):
            raise ValueError("El dni debe ser un entero")
        self.__dni = dni
        
    def setNombre(self,nombre:str):
        if not isinstance(nombre,str) or nombre in [""," ",None]:
            raise ValueError("El nombre debe ser un string")
        self.__nombre = nombre
    
    def setApellido(self,apellido:str):
        if not isinstance(apellido,str) or apellido in [""," ",None]:
            raise ValueError("El apellido debe ser un string")
        self.__apellido = apellido
        
    def setMail(self,mail:str):
        if not isinstance(mail,str) or mail in [""," ",None]:
            raise ValueError("El mail debe ser un string")
        self.__mail = mail
    
    def setFechaNacimiento(self,fecha_nacimiento:str):
        if not isinstance(fecha_nacimiento,str):
            raise ValueError("La fecha de nacimiento debe ser un datetime.date")
        self.__fecha_nacimiento = fecha_nacimiento
        
    