import json

class Libro:
    def __init__(self,titulo:str,autor:str,genero:str,año_publicacion: int,isbn: int):
        if not isinstance(titulo,str) or titulo.isspace():
            raise ValueError("El titulo del libro no puede ser vacio")
        if not isinstance(autor,str) or autor.isspace():
            raise ValueError("El autor del libro no puede ser vacio")
        if not isinstance(genero,str) or genero.isspace():
            raise ValueError("El genero del libro no puede ser vacio")
        if not isinstance(año_publicacion,int) or año_publicacion < 0:
            raise ValueError("El año de publicacion del libro no puede ser negativo")
        if not isinstance(isbn,int) or isbn < 0:
            raise ValueError("El isbn del libro no puede ser negativo")
        
        self.__titulo: str = titulo
        self.__autor: str = autor
        self.__genero: str = genero
        self.__año_publicacion: int = año_publicacion
        self.__isbn: int = isbn

        with open("libros.json", encoding="utf-8") as json_file:
            data = json.load(json_file)
            data.append(self.to_json())
        
    @property
    def titulo(self):
        return self.__titulo
    @property
    def autor(self):
        return self.__autor
    @property
    def genero(self):
        return self.__genero
    @property
    def año_publicacion(self):
        return self.__año_publicacion
    @property
    def isbn(self):
        return self.__isbn
    
    @titulo.setter
    def titulo(self,titulo):
        if not isinstance(titulo,str) or titulo.isspace():
            raise ValueError("El titulo del libro no puede ser vacio")
        self.__titulo = titulo
    
    @autor.setter
    def autor(self,autor):
        if not isinstance(autor,str) or autor.isspace():
            raise ValueError("El autor del libro no puede ser vacio")
        self.__autor = autor
        
    @genero.setter
    def genero(self,genero):
        if not isinstance(genero,str) or genero.isspace():
            raise ValueError("El genero del libro no puede ser vacio")
        self.__genero = genero
        
    @año_publicacion.setter
    def año_publicacion(self,año_publicacion):
        if not isinstance(año_publicacion,int) or año_publicacion < 0:
            raise ValueError("El año de publicacion del libro no puede ser negativo")
        self.__año_publicacion = año_publicacion
    
    @isbn.setter
    def isbn(self,isbn):
        if not isinstance(isbn,int) or isbn < 0:
            raise ValueError("El isbn del libro no puede ser negativo")
        self.__isbn = isbn
    
    def to_json(self):
        """
        Metodo que convierte los datos del libro en un diccionario y luego en un json
        Returns:
            _type_: _description_
        """
        dicc = {
            'titulo': self.__titulo,
            'autor': self.__autor,
            'genero': self.__genero,
            'año_publicacion': self.__año_publicacion,
            'isbn': self.__isbn
        }
        return json.dumps(dicc,ensure_ascii=False)
    
    @classmethod
    def from_json(cls,json_data):
        """
        Metodo que recibe un json y lo convierte en un diccionario, luego crea un objeto libro con esos datos
        Args:
            json_data
        Returns:
           cls: objeto libro
        """
        datos = json.loads(json_data)
        return cls(datos['titulo'],datos['autor'],datos['genero'],datos['año_publicacion'],datos['isbn'])
    
    
if __name__ == "__main__":
    libro_1 = Libro("El señor de los anillos","J.R.R. Tolkien","Fantasia",1954,9788445073801)
    libro_2 = Libro("Harry Potter y la piedra filosofal","J.K. Rowling","Fantasia",1997,9788478884459)
    
    json_libro_1 = libro_1.to_json()
    print(json_libro_1) 
    libro_3 = Libro.from_json(json_libro_1)
    
    with open("libros.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
        json_file.close()
        
    for i in range(len(data)):
        libro = Libro.from_json(json.dumps(data[i],ensure_ascii=False))
        print(libro.titulo, libro .autor, libro.genero, libro.año_publicacion, libro.isbn)
    
    while True:
        try:
            año_ingresado = int(input("Ingrese un año para buscar los libros publicados: "))
            if año_ingresado <= 0:
                raise ValueError("El año debe ser mayor a 0")
            break
        except ValueError as e:
            print(f"Error: {e}")  
              
    with open("libros.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            libro = Libro.from_json(json.dumps(data[i], ensure_ascii=False))
            if libro.año_publicacion == año_ingresado:
                print(libro.titulo, libro.autor, libro.genero, libro.año_publicacion, libro.isbn)
                se_encontraron_libros = True
            else:
                se_encontraron_libros = False
                
        if not se_encontraron_libros:
            print("No se encontraron libros publicados en ese año")    
        json_file.close()
                    
            
            
        
                    
            
            
        