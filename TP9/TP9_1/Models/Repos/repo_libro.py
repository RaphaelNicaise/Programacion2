from Models.Entities.libro import Libro
import json

class RepoLibro:
    PATH = "Data/libros.json"
    
    def __init__(self):
        self.libros: list['Libro'] = self.cargarLibros()
        
    def cargarLibros(self):
        """
        Metodo para cargar libros al inicializarse el repositorio
        """
        lista: list['Libro'] = []
        try:
            
            with open(RepoLibro.PATH, 'r') as file:
                libros_data = json.load(file)
                for libro in libros_data:
                    lista.append(Libro.fromDict(libro))
            
        except FileNotFoundError:
            print('No se encontró el archivo')

        return lista
    
    def guardarLibros(self):
        try:
            lista = [libro.toDict() for libro in self.libros]
        
            with open(RepoLibro.PATH, 'w') as file:
                json.dump(lista, file, indent=4)
                
        except FileNotFoundError:
            print('No se encontró el archivo')
    
    def getLibros(self)->list['Libro']:
        return self.libros 
    
    def getLibro(self,isbn: str)->Libro:
        for libro in self.libros:
            if libro.getISBN() == isbn:
                return libro
    
    def existe(self, otroLibro: Libro)->bool:
        for libro in self.libros:
            if libro == otroLibro:
                return True
        return False
    
    def existeISBN(self,isbn: str)->bool:
        for libro in self.libros:
            if libro.getISBN() == isbn:
                return True
    
    def agregarLibro(self,nuevoLibro: Libro):
        if not isinstance(nuevoLibro, Libro):
            raise ValueError('El objeto no es un libro')
        if self.existe(nuevoLibro):
            raise ValueError('El libro ya existe')
        self.libros.append(nuevoLibro)
        self.guardarLibros()  
          
    def modificarPorISBN(self,isbn: str, titulo: str, autor: str, anio: int, genero: str)->bool:
        for libro in self.libros:
            if libro.getISBN() == isbn:
                libro.setTitulo(titulo)
                libro.setAutor(autor)
                libro.setAnio(anio)
                libro.setGenero(genero)
                self.guardarLibros()
                return True
        return False
    
    def eliminarPorISBN(self, isbn: str):
        for libro in self.libros:
            if libro.getISBN() == isbn:
                self.libros.remove(libro)
                self.guardarLibros()
                return True
        return False