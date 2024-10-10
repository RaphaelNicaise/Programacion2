class Pais:
    
    def __init__(self,codigo:str,nombre:str,cantidadDispositivos:int=3):
        if not isinstance(codigo,str): raise ValueError
        if not isinstance(nombre,str): raise ValueError
        if not isinstance(cantidadDispositivos, int) or not (0 <= cantidadDispositivos <= 4): raise ValueError("Cantidad de dispositivos no es valida")
        
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidadDispositivos = cantidadDispositivos
        
    # Comandos
    
    def establecerCodigo(self,codigo:str):
        if not isinstance(codigo,str): raise ValueError("Codigo no es valido")
        self.__codigo = codigo
        
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str): raise ValueError("Nombre no es valido")
        self.__nombre = nombre
    
    def establecerCantidadDispositivos(self,cantidadDispositivos:int):
        if not isinstance(cantidadDispositivos, int) or not (0 <= cantidadDispositivos <= 4): raise ValueError("Cantidad de dispositivos no es valida")
        self.__cantidadDispositivos = cantidadDispositivos
        
    # Consultas
    
    def obtenerCodigo(self)->str: return self.__codigo
    
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerCantidadDispositivos(self)->int: return self.__cantidadDispositivos

class Suscripcion:
    def __init__(self,nombre:str,email:str,telefono:str,pais:'Pais'):
        
        for var in [nombre,email,telefono]:
            if not isinstance(var,str):
                raise ValueError("Nombre, email o telefono no es valido")
        
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self._playlists = []
        self._dispositivos = []
     
    # Comandos
        
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("Nombre no es valido")
        self._nombre = nombre
        
    def establecerEmail(self,email:str):
        if not isinstance(email,str):
            raise ValueError("Email no es valido")
        self._email = email
        
    def establecerTelefono(self,telefono:str):
        if not isinstance(telefono,str):
            raise ValueError("Telefono no es valido")
        self._telefono = telefono
        
    def crearPlaylist(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("Nombre no es valido")
        playlist = Playlist(nombre)
        playlist.asignarDuenio(self)
        self._playlists.append(playlist)
        return playlist
    
    def agregarCancion(self,playlist:'Playlist',cancion:'Cancion'):
        if not isinstance(playlist,Playlist) or not isinstance(cancion,Cancion):
            raise ValueError("No es una playlist o cancion valida")
        if playlist not in self._playlists: # Solo se pueden agregar canciones el duenio de la playlist
            raise ValueError("No es el duenio de la playlist")
        
        playlist.agregarCancion(cancion)
        
    def eliminarCancion(self,playlist:'Playlist',cancion:'Cancion'):
        if not isinstance(playlist,Playlist) or not isinstance(cancion,Cancion):
            raise ValueError("No es una playlist o cancion valida")
        if playlist not in self.__playlists:
            raise ValueError("No es el duenio de la playlist")
        playlist.eliminarCancion(cancion)
    
    def agregarDispositivo(self,dispositivo:'Dispositivo'):
        if not isinstance(dispositivo,Dispositivo):
            raise ValueError("No es un dispositivo valido")
        self._dispositivos.append(dispositivo)
        dispositivo.asignarSuscripcion(self)      
    # Consultas
    
    def obtenerNombre(self)->str: return self._nombre
    def obtenerEmail(self)->str: return self._email
    def obtenerTelefono(self)->str: return self._telefono
    def obtenerPlaylists(self)->list['Playlist']: return self._playlists
    def obtenerDispositivos(self)->list['Dispositivo']: return self._dispositivos
    
class SuscripcionGratis(Suscripcion):
    def __init__(self,nombre:str,email:str,telefono:str,pais:'Pais'):
        super().__init__(nombre,email,telefono,pais)
        self.__tiempoReproducido = 0
        self.__tiempoSinPublicidad = 0
        
    # Comandos
    
    def reproducirMusica(self):
        pass
    
    def interruimpirConPublicidad(self):
        pass
    
    def agregarDispositivo(self, dispositivo):
        if not isinstance(dispositivo,Dispositivo):
            raise ValueError("No es un dispositivo valido")
        if len(self._dispositivos) >= 1:
            raise ValueError("No se pueden agregar mas dispositivos")
        self._dispositivos.append(dispositivo)
        
    # Consultas
    
    def obtenerTiempoReproducido(self)->int: return self.__tiempoReproducido
    def obtenerTiempoSinPublicidad(self)->int: return self.__tiempoSinPublicidad
    
    
class SuscripcionPaga(Suscripcion):
    def __init__(self,nombre:str,email:str,telefono:str,pais:'Pais'):
        super().__init__(nombre,email,telefono,pais)
        self.__MaxDispositivos = pais.obtenerCantidadDispositivos()
    # Comandos
    
    def reproducirMusica(self):
        pass
    
    def descargarMusica(self):
        pass
    
    def elegirCancion(self):
        pass
    
    def habilitarDispositivo(self):
        pass
    
    def agregarDispositivo(self, dispositivo):
        if not isinstance(dispositivo,Dispositivo):
            raise ValueError("No es un dispositivo valido")
        if len(self._dispositivos) >= self.__MaxDispositivos:
            raise ValueError("No se pueden agregar mas dispositivos")
        self._dispositivos.append(dispositivo)
        
    # Consultas
    
    def obtenerDispositivos(self)->list['Dispositivo']: return self._dispositivos
    def obtenerMaxDispositivos(self)->int: return self.__MaxDispositivos
    
class Dispositivo:
    
    ID_DISPOSITIVO = 23571321305 # Codigo Autoincremental que arranca en 23571321305
    
    def __init__(self,nombre:str,tipo:str):
        if not isinstance(nombre,str): raise ValueError("Nombre no es valido")
        if not isinstance(tipo,str): raise ValueError("Tipo no es valido")
        self.__id = Dispositivo.ID_DISPOSITIVO
        Dispositivo.ID_DISPOSITIVO += 1
        self.__nombre = nombre
        self.__tipo = tipo
        self.__suscripcion = None
    
    def __str__(self):
        return f"Id: {self.__id} - {self.__nombre} - {self.__tipo}"
    
    def __repr__(self):
        return f"{self.__id}"
    # Comandos
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str): raise ValueError("Nombre no es valido")
        self.__nombre = nombre
    def establecerTipo(self,tipo:str):
        if not isinstance(tipo,str): raise ValueError("Tipo no es valido")
        self.__tipo = tipo
        
    def asignarSuscripcion(self,suscripcion:'Suscripcion'):
        if not isinstance(suscripcion,Suscripcion): raise ValueError("No es una suscripcion valida")
        self.__suscripcion = suscripcion
    
    # Consultas
    def obtenerId(self)->int: return self.__id
    def obtenerNombre(self)->str: return self.__nombre
    def obtenerTipo(self)->str: return self.__tipo
    
class Playlist:
    
    CONTADOR_PLAYLIST = 1000 # Codigo Autoincremental que arranca en 1000
    
    def __init__(self,nombre:str):
        if not isinstance(nombre,str): raise ValueError("Nombre no es valido")
        self.__nombre = nombre
        self.__canciones: list[Cancion] = []
        self.__duenio = None
        self.__codigo = Playlist.CONTADOR_PLAYLIST
        Playlist.CONTADOR_PLAYLIST += 1 # Sumamos uno al contador de playlist
    
    def __str__(self):
        return f"{self.__nombre}"
    
    def __repr__(self):
        return f"{self.__codigo}"
    # Comandos
    
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str): raise ValueError
        self.__nombre = nombre
        
    def agregarCancion(self,cancion:'Cancion'):
        
        if not isinstance(cancion,Cancion): raise ValueError(" No es una cancion valida")
        if cancion in self.__canciones: raise ValueError("La cancion ya esta en la playlist")
        self.__canciones.append(cancion)
        
    def eliminarCancion(self,cancion:'Cancion'):
        
        if not isinstance(cancion,Cancion) or cancion not in self.__canciones: raise ValueError("No es una cancion valida")
        if cancion not in self.__canciones: raise ValueError("La cancion no esta en la playlist")
        self.__canciones.remove(cancion)
        
    def asignarDuenio(self,suscripcion:'Suscripcion'):
        if not isinstance(suscripcion,Suscripcion): raise ValueError("No es una suscripcion valida")
        self.__duenio = suscripcion
    
    # Consultas
    def obtenerCodigo(self)->int: return self.__codigo
    
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerCanciones(self)->list['Cancion']: return self.__canciones
    
    def obtenerDuenio(self)->'Suscripcion': return self.__duenio
    
    
    
class Cancion:
    
    CODIGO_CANCION = 41239 # Codigo Autoincremental que arranca en 412342
    
    def __init__(self,nombre:str,duracion:int,genero:str): # To Do: agregar artista-banda, tambien clase artista-banda
        if not isinstance(nombre,str): raise ValueError("Nombre no es valido")
        if not isinstance(duracion,int) or duracion <= 0: raise ValueError("Duracion no es valida")
        if not isinstance(genero,str): raise ValueError("Genero no es valido")
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero
        self.__codigo = Cancion.CODIGO_CANCION
        Cancion.CODIGO_CANCION += 1
    
    def __str__(self):
        return f"{self.__nombre} - {self.__duracion}:00 | {self.__genero} "
    
    def __repr__(self):
        return f"{self.__codigo}"
    # Comandos
    
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str): raise ValueError("Nombre no es valido")
        self.__nombre = nombre
        
    def establecerDuracion(self,duracion:int):
        if not isinstance(duracion,int) or duracion <= 0: raise ValueError("Duracion no es valida")
        self.__duracion = duracion
        
    def establecerGenero(self,genero:str):
        if not isinstance(genero,str): raise ValueError("Genero no es valido")
        self.__genero = genero
        
    def reproducir(self):
        pass
    
    # Consultas
    
    def obtenerNombre(self)->str: return self.__nombre
    def obtenerDuracion(self)->int: return self.__duracion
    def obtenerGenero(self)->str: return self.__genero
    
class Tester:
    @staticmethod
    def run():
    
        pais1 = Pais("AR","Argentina",4)
        pais2 = Pais("UY","Uruguay")
        
        suscripcion1 = SuscripcionGratis("Juan","juan@gmail.com","+123456",pais1)
        suscripcion2 = SuscripcionPaga("Pedro","pedro@gmail.com","+123456",pais2)
        
        cancion1 = Cancion("Have You ever seen the Rain", 3, "Rock")
        cancion2 = Cancion("Despacito", 4, "Reagueton")
        cancion3 = Cancion("La Cumparsita", 2, "Tango")
        cancion4 = Cancion("Por Mil Noches", 3, "Rock")
        cancion5 = Cancion("La Balsa", 3, "Rock")
        cancion6 = Cancion("All My Loving",4,"Rock")
        cancion7 = Cancion("Yesterday",3,"Rock")
        cancion8 = Cancion("Let It Be",4,"Rock")
        cancion9 = Cancion("Mardy Bum",3,"Rock")
        
        playlist1 = suscripcion1.crearPlaylist("Broken Dreams")
        suscripcion1.agregarCancion(playlist1,cancion1)
        suscripcion1.agregarCancion(playlist1,cancion6)
        suscripcion1.agregarCancion(playlist1,cancion7)
        suscripcion1.agregarCancion(playlist1,cancion8)
        suscripcion1.agregarCancion(playlist1,cancion9)
        
        playlist2 = suscripcion1.crearPlaylist("Rock Nacional")
        suscripcion1.agregarCancion(playlist2,cancion4)
        suscripcion1.agregarCancion(playlist2,cancion5)
        
        print(f"Playlists de suscriptor 1: {suscripcion1.obtenerPlaylists()}")
        print(f"Canciones playlist1: {playlist1.obtenerCanciones()}")
        print(f"Canciones playlist2: {playlist2.obtenerCanciones()}")
        
        for playlist in suscripcion1.obtenerPlaylists():
            print(f"Playlist: {playlist} - Canciones:")
            for cancion in playlist.obtenerCanciones():
                print(f" • {cancion}")
                
        try:
            suscripcion2.agregarCancion(playlist1,cancion1) # -> ERROR: No es el duenio de la playlist
        except ValueError as error:
            print(error)
        
        dispositivo1 = Dispositivo("Smartphone1","Movil")
        dispositivo2 = Dispositivo("Smart TV2","TV")
        dispositivo3 = Dispositivo("Notebook3","PC")
        
        suscripcion1.agregarDispositivo(dispositivo1)
        try:
            suscripcion1.agregarDispositivo(dispositivo2) # -> ERROR: No se pueden agregar mas dispositivos ya que es una suscripcion gratis
        except ValueError as error:
            print(error)
        
        suscripcion2.agregarDispositivo(dispositivo2)
        suscripcion2.agregarDispositivo(dispositivo3)
        print(f"Dispositivos suscriptor 1: {suscripcion1.obtenerDispositivos()}")
        print(f"Dispositivos suscriptor 2: {suscripcion2.obtenerDispositivos()}")
                    
        
            
if __name__ == '__main__':
    Tester.run()