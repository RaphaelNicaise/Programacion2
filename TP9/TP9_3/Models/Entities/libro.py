class Libro:
    
    def __init__(self, titulo: str, autor: str, genero: str, anio: int, ISBN: str, ejemplares: int):
        if not isinstance(titulo, str) or titulo in ['', None, ' ']:
            raise ValueError(f'El titulo debe ser un string')
        if not isinstance(autor, str) or autor in ['', None, ' ']:
            raise ValueError(f'El autor debe ser un string')
        if not isinstance(genero, str) or genero in ['', None, ' ']:
            raise ValueError(f'El genero debe ser un string')
        if not isinstance(anio, int) or anio < 0:
            raise ValueError(f'El año debe ser un entero positivo')
        if not isinstance(ISBN, str) or ISBN in ['', None, ' ']:
            raise ValueError(f'El ISBN debe ser un string')
        
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio = anio
        self.__ISBN = ISBN
        self.__ejemplares = ejemplares
    
    def __eq__(self, otroLibro: 'Libro'):
        return self.getISBN() == otroLibro.getISBN()
        
    #getters
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getGenero(self):
        return self.__genero
    
    def getAnio(self):
        return self.__anio
    
    def getISBN(self):
        return self.__ISBN
    
    def getEjemplares(self):
        return self.__ejemplares
    
    # Setters
    
    def setTitulo(self, titulo):
        if not isinstance(titulo, str) or titulo in ['', None, ' ']:
            raise ValueError(f'El titulo debe ser un string')
        self.__titulo = titulo
        
    def setAutor(self, autor):
        if not isinstance(autor, str) or autor in ['', None, ' ']:
            raise ValueError(f'El autor debe ser un string')
        self.__autor = autor
        
    def setGenero(self, genero):
        if not isinstance(genero, str) or genero in ['', None, ' ']:
            raise ValueError(f'El genero debe ser un string')
        self.__genero = genero
        
    def setAnio(self, anio):
        if not isinstance(anio, int) or anio < 0:
            raise ValueError(f'El año debe ser un entero positivo')
        self.__anio = anio
        
    def setISBN(self, ISBN):
        if not isinstance(ISBN, str) or ISBN in ['', None, ' ']:
            raise ValueError(f'El ISBN debe ser un string')
        self.__ISBN = ISBN
        
    def setEjemplares(self, ejemplares):
        self.__ejemplares = ejemplares
    
    def restar_ejemplar(self):
        if not self.getEjemplares() > 0:
            raise ValueError(f'No hay ejemplares disponibles')
        
        self.setEjemplares(self.getEjemplares() - 1)
        
    @classmethod
    def fromDict(cls, diccionario: dict):
        
        if not isinstance(diccionario, dict):
            raise ValueError(f'El diccionario debe ser un diccionario')
        if not 'titulo' in diccionario:
            raise ValueError(f'El diccionario no tiene la clave titulo')
        if not 'autor' in diccionario:
            raise ValueError(f'El diccionario no tiene la clave autor')
        if not 'genero' in diccionario:
            raise ValueError(f'El diccionario no tiene la clave genero')
        if not 'anio' in diccionario:
            raise ValueError(f'El diccionario no tiene la clave anio')
        if not 'ISBN' in diccionario:
            raise ValueError(f'El diccionario no tiene la clave ISBN')
        if not 'ejemplares' in diccionario:
            raise ValueError(f'El diccionario no tiene la clave ejemplares')
        
        return cls(diccionario['titulo'], diccionario['autor'], diccionario['genero'], diccionario['anio'], diccionario['ISBN'], diccionario['ejemplares'])
        
    
    
    def toDict(self):
        return {
            'titulo': self.__titulo,
            'autor': self.__autor,
            'genero': self.__genero,
            'anio': self.__anio,
            'ISBN': self.__ISBN,
            'ejemplares': self.__ejemplares
        }
    