class Cuidador:
    def __init__(self,nombre:str,direccion:str,telefono:str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascotas = []
     
    def __str__(self)->str:
        return f"Cuidador: {self.__nombre} - {self.__direccion} - {self.__telefono}"   
    
    def __repr__(self)->str:
        return f"{self.__nombre}"    

    # Comandos
    
    def establecerNombre(self, nombre: str):
        self.__nombre = nombre

    def establecerDireccion(self, direccion: str):
        self.__direccion = direccion

    def establecerTelefono(self, telefono: str):
        self.__telefono = telefono

    def AsignarMascota(self, mascota: 'Mascota'):
        if not isinstance(mascota,Mascota):
            raise ValueError("Error: No es una mascota")
        
        if mascota not in self.__mascotas:
            if mascota.obtenerCuidador() != None: # Si tiene cuidador, se lo desasigno al Cuidador
                mascota.obtenerCuidador().desasignarMascota(mascota)
            self.__mascotas.append(mascota) # Y le asigno la mascota al nuevo Cuidador
            mascota.establecerCuidador(self) # Y le asigno el Cuidador a la mascota
                
            # cambiar de cuidador
    
    def desasignarMascota(self, mascota: 'Mascota'):
        if not isinstance(mascota,Mascota):
            raise ValueError("Error: No es una mascota")
        
        if mascota in self.__mascotas:
            self.__mascotas.remove(mascota)
                   
    # Consultas
    
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerDireccion(self)->str: return self.__direccion
    
    def obtenerTelefono(self)->str: return self.__telefono
    
    def obtenerMascotas(self)->list: return self.__mascotas
    
class Mascota:
    def __init__(self,nombre:str,especie:str,edad:int,descripcion:str):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion
        self.__cuidador = None
        
    def __str__(self)->str:
        msg = f"Mascota: {self.__nombre} - {self.__especie} - {self.__edad} - {self.__descripcion}"
        if self.__cuidador == None:
            return f"{msg} Sin cuidador"
        return f"{msg} Cuidador: {self.__cuidador.obtenerNombre()}"
    
    def __repr__(self)->str:
        return f"({self.__nombre},{self.__especie})"
    
    # Comandos
    
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre

    def establecerEspecie(self, especie: str):
        self.__especie = especie

    def establecerEdad(self, edad: int):
        self.__edad = edad

    def establecerDescripcion(self, descripcion: str):
        self.__descripcion = descripcion
    
    def establecerCuidador(self, cuidador: 'Cuidador'):
        if not isinstance(cuidador,Cuidador):
            raise ValueError("Error: No es un cuidador")
        
        if self.__cuidador is not None:
            self.__cuidador.desasignarMascota(self)  
        self.__cuidador = cuidador
        
    # Consultas 
    
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerEspecie(self)->str: return self.__especie
    
    def obtenerEdad(self)->int: return self.__edad
    
    def obtenerDescripcion(self)->str: return self.__descripcion
    
    def obtenerCuidador(self)->'Cuidador': return self.__cuidador
    
        
class Tester:
    @staticmethod
    def runtest():
        cuidador1 = Cuidador("Juan","San Martin 123","123456789")
        cuidador2 = Cuidador("Pedro","Belgrano 456","987654321")
        mascota1 = Mascota("Firulais","Perro",5,"Perro de raza")
        print(cuidador1)
        print(mascota1)
        cuidador1.AsignarMascota(mascota1)
        print(cuidador1.obtenerMascotas())
        print(mascota1)
        cuidador2.AsignarMascota(mascota1)
        print(mascota1)
        print(cuidador1.obtenerMascotas())
        print(cuidador2.obtenerMascotas())
        print(mascota1)
        cuidador1.AsignarMascota(mascota1)
        print(cuidador1.obtenerMascotas())
        print(cuidador2.obtenerMascotas())
        print(mascota1)

if __name__ == "__main__":
    Tester.runtest()        
    
    