from dataclasses import dataclass,field

@dataclass
class Dueño:
    _nombre: str
    _apellido: str
    _mail: str
    _edad: int = field(default=1)
    _perros: list['Perro'] = field(default_factory=list)

    def __post_init__(self):
        if self.edad <= 0:
            raise ValueError('Edad debe ser mayor a 0')

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def mail(self):
        return self._mail
    
    @property
    def perros(self):
        return self._perros
    
    @nombre.setter
    def nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError('Nombre debe ser una cadena de texto')
        self._nombre = nombre
    
    @edad.setter
    def edad(self, edad: int):
        if not isinstance(edad, int):
            raise TypeError('Edad debe ser un entero')
        if edad < 0:
            raise ValueError('Edad no puede ser negativa')
        self._edad = edad
        
    @apellido.setter
    def apellido(self, apellido: str):
        if not isinstance(apellido, str):
            raise TypeError('Apellido debe ser una cadena de texto')
        self._apellido = apellido
        
    @mail.setter
    def mail(self, mail: str):
        if not isinstance(mail, str):
            raise TypeError('Mail debe ser una cadena de texto')
        self._mail = mail
    
    def addPerro(self, perro):
        if not isinstance(perro, Perro):
            raise TypeError('Debe ser un perro')
        if perro in self._perros:
            raise ValueError('El perro ya existe')
        self._perros.append(perro)

@dataclass
class Perro:
    __nombre: str
    __edad: int
    
    def __post_init__(self):
        if self.edad <= 0:
            raise ValueError('Edad debe ser mayor a 0')
        
    @classmethod
    def from_json(cls, json):
        nombre = json['nombre']
        edad = json['edad']
        return cls(nombre, edad)      
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property # getEdad pero como atributo de la clase
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def nombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise TypeError('Nombre debe ser una cadena de texto')
        self.__nombre = nombre
    
    @edad.setter # setEdad pero como atributo de la clase
    def edad(self, edad: int):
        if not isinstance(edad, int):
            raise TypeError('Edad debe ser un entero')
        if edad < 0:
            raise ValueError('Edad no puede ser negativa')
        self.__edad = edad
        
        
        
if __name__ == '__main__':
    p = Perro('Firulais', 5)
    print(p)
    p.edad = 6
    print(p)

    d = Dueño('Juan', 'Perez',"raphanicaise@gmail.com", 25)
    print(d.perros)
    d.addPerro(p)
    print(d.perros)
