import json

class Contacto:
    def __init__(self,nombre:str,apellido:str,telefono:str,correo:str,direccion:str):
        
        if not isinstance(nombre,str) or nombre in [""," "]:
            raise ValueError("El nombre del contacto no puede ser vacio")
        if not isinstance(apellido,str) or apellido in [""," "]:
            raise ValueError("El apellido del contacto no puede ser vacio")
        if not isinstance(telefono,str) or telefono in [""," "]:
            raise ValueError("El telefono del contacto no puede ser vacio")
        if not isinstance(correo,str) or correo in [""," "]:
            raise ValueError("El correo del contacto no puede ser vacio")
        if not isinstance(direccion,str) or direccion in [""," "]:
            raise ValueError("La direccion del contacto no puede ser vacio")
        
        self.__nombre: str  = nombre
        self.__apellido: str = apellido
        self.__telefono: str = telefono
        self.__correo: str = correo
        self.__direccion: str = direccion
        
    def __dict__(self):
        return {
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "telefono": self.__telefono,
            "correo": self.__correo,
            "direccion": self.__direccion
        }
    
    def to_json(self):
        return self.__dict__()
        
    def __str__(self):
        pass
    
    def __repr__(self):
        return f"({self.__nombre} {self.__apellido}, {self.__telefono})"
    
    @property
    def nombre(self): return self.__nombre
    
    @property
    def apellido(self): return self.__apellido
    
    @property
    def telefono(self): return self.__telefono
    
    @property
    def correo(self): return self.__correo
    
    @property
    def direccion(self): return self.__direccion
    
    @nombre.setter
    def nombre(self,nombre):
        if not isinstance(nombre,str) or nombre.isspace():
            raise ValueError("El nombre del contacto no puede ser vacio")
        self.__nombre = nombre
        
    @apellido.setter
    def apellido(self,apellido):
        if not isinstance(apellido,str) or apellido.isspace():
            raise ValueError("El apellido del contacto no puede ser vacio")
        self.__apellido = apellido
        
    @telefono.setter
    def telefono(self,telefono):
        if not isinstance(telefono,str) or telefono.isspace():
            raise ValueError("El telefono del contacto no puede ser vacio")
        self.__telefono = telefono
    
    @correo.setter
    def correo(self,correo):
        if not isinstance(correo,str) or correo.isspace():
            raise ValueError("El correo del contacto no puede ser vacio")
        self.__correo = correo
        
    @direccion.setter
    def direccion(self,direccion):
        if not isinstance(direccion,str) or direccion.isspace():
            raise ValueError("La direccion del contacto no puede ser vacio")
        self.__direccion = direccion

    @classmethod
    def from_json(cls,json_data):
        return cls(**json_data)
    
class Tester:
    @staticmethod
    def run():
        c1 = Contacto("Juan","Perez","123456","juanperez@gmail.com","Calle 123")
        
        try:
            c1.nombre = " " # Asignar a propiedad, hace la validacion 
        except ValueError as e:
            print(e)
        
        
        lista_contactos:list = []
        
        # leer de un archivo json
        with open("contactos.json","r",encoding="utf-8") as json_file:
            data = json.load(json_file) 
        
            for contacto in data:
                contacto = Contacto.from_json(contacto)
                lista_contactos.append(contacto)    
            json_file.close()
        
        print(lista_contactos)
        
        # escribir en un archivo json
        with open("contactos.json","w",encoding="utf-8") as json_file:
           json.dump([contacto.to_json() for contacto in lista_contactos],json_file,indent=4)

        

if __name__ == '__main__':
    Tester.run()
        
    