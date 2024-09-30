from modulo_fecha import Fecha
class Evento:
    def __init__(self,nombre:str,fecha:'Fecha',descripcion:str) -> None:
        
        if not isinstance(fecha,Fecha):
            raise ValueError("Debe ser un objeto de tipo fecha")
        
        self.__nombre = nombre    
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__organizador = None
        self.__participantes = []
        
        
    def __str__(self):
        msg = f"Evento: {self.__nombre} Fecha: {self.__fecha} Descripcion: {self.__descripcion}"
        if self.__organizador != None: msg += f" Organizador: {self.__organizador}"
        return msg
    
    def __repr__(self):
        return self.__nombre
    
    # Comandos
    
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    def establecerFecha(self,fecha:'Fecha'):
        if not isinstance(fecha,Fecha):
            raise ValueError("Debe ser un objeto de tipo fecha")
    
        self.__fecha = fecha
    
    def establecerDescripcion(self,descripcion:str):
        self.__descripcion = descripcion
    
    def establecerOrganizador(self,organizador:'Organizador'):
        if self.__organizador != None:
            self.__organizador.obtenerEventos().remove(self)
        self.__organizador = organizador
        self.__organizador.agregarAEvento(self)

    def agregarParticipante(self,participante:'Participante'):
        if participante not in self.__participantes:    
            self.__participantes.append(participante)
            participante.agregarAEvento(self)
            
    def agregarParticipantes(self,listaParticipantes:list):
        for participante in listaParticipantes:
            if isinstance(participante,Participante):
                self.agregarParticipante(participante)        

    # Consultas
    
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerFecha(self)->'Fecha': return self.__fecha

    def obtenerDescripcion(self)->str: return self.__descripcion
    
    def obtenerOrganizador(self)->'Organizador': return self.__organizador
    
    def obtenerParticipantes(self)->list: return self.__participantes
    
class Participante:
    def __init__(self,nombre:str,correo:str,telefono:str):
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__eventos = []
        
    def __str__(self):
        return f"Nombre: {self.__nombre} Correo: {self.__correo} Telefono: {self.__telefono}"
    
    def __repr__(self):
        return self.__nombre
    
    # Comandos
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    def establecerCorreo(self,correo:str):
        self.__correo = correo
        
    def establecerTelefono(self,telefono:str):
        self.__telefono = telefono
  
    def agregarAEvento(self,evento:'Evento'):
        if isinstance(evento,Evento):
            if evento not in self.__eventos:
                self.__eventos.append(evento)
    
    # Consultas
    
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerCorreo(self)->str: return self.__correo
    
    def obtenerTelefono(self)->str: return self.__telefono
    
    def obtenerEventos(self)->list: return self.__eventos

class Organizador:
    def __init__(self,nombre:str,correo:str,especialidad:str):
        self.__nombre = nombre
        self.__correo = correo
        self.__especialidad = especialidad
        self.__eventos = []
        
    def __str__(self):
        return f"Nombre: {self.__nombre} Correo: {self.__correo} Especialidad: {self.__especialidad}"
    
    def __repr__(self):
        return self.__nombre 
    
    # Comandos
    
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
        
    def establecerCorreo(self,correo:str):
        self.__correo = correo
        
    def establecerEspecialidad(self,especialidad:str):
        self.__especialidad = especialidad
        
    def agregarAEvento(self,evento:'Evento'):
        if isinstance(evento,Evento):
            if evento not in self.__eventos:
                self.__eventos.append(evento)
    # Consultas
       
    def obtenerNombre(self)->str: return self.__nombre
    
    def obtenerCorreo(self)->str: return self.__correo
    
    def obtenerEspecialidad(self)->str: return self.__especialidad
    
    def obtenerEventos(self)->list: return self.__eventos
       
class Tester:
    @staticmethod
    def runtest():
        # Eventos
        evento_1 = Evento("Lollapalooza",Fecha(12,12,2024),"Lo mejor del mundo en capi")
        evento_2 = Evento("Cosquin Rock",Fecha(21,2,2025),"Rock de cordoba papa")
        
        # Organizador
        organizador_1 = Organizador("Flow","flow@gmail.com","Empresa de eventos")
        organizador_2 = Organizador("José Palazzo","josepalazzo@hotmail.com","Abogado-Empresario")
        organizador_3 = Organizador("Pablo Lescano","pablitolescano@gmail.com","Musico-Empresario")
        
        # Participantes
        part_1 = Participante("Juan Perez", "juan.perez@example.com", "123456789")
        part_2 = Participante("Maria Gomez", "maria.gomez@example.com", "987654321")
        part_3 = Participante("Carlos Lopez", "carlos.lopez@example.com", "456123789")
        part_4 = Participante("Ana Martinez", "ana.martinez@example.com", "789456123")
        part_5 = Participante("Luis Rodriguez", "luis.rodriguez@example.com", "321654987")
        part_6 = Participante("Sofia Fernandez", "sofia.fernandez@example.com", "654987321")
        
        evento_1.establecerOrganizador(organizador_1) # establecemos organizador_1 como organizador del evento_1
        evento_1.agregarParticipante(part_1) # 
        lista_participantes_nuevos = [part_1,part_2,part_3,part_4,part_5] 
        evento_1.agregarParticipantes(lista_participantes_nuevos) # Agregamos al evento a todos los de la lista, siempre y cuando no se repita
        print(f"Participantes del evento {evento_1.obtenerNombre()}->",evento_1.obtenerParticipantes())
        print(f"Eventos de {part_1.obtenerNombre()}->",part_1.obtenerEventos())
        
        evento_2.establecerOrganizador(organizador_2) # Establecemos organizador_2 como organizador del evento_2
        evento_2.agregarParticipantes([part_1,part_2,part_6]) # Agregamos al evento a los participantes de la lista
        print(f"Participantes del evento {evento_2.obtenerNombre()}->",evento_2.obtenerParticipantes()) 
        print(f"Organizador de evento {evento_2.obtenerNombre()}-> {evento_2.obtenerOrganizador()}")
        print(f"Eventos a los que va {part_1.obtenerNombre()}->",part_1.obtenerEventos())
        evento_2.establecerOrganizador(organizador_1) # Cambiamos el organizador del evento_2 a organizador_1
        print(f"Eventos de organizador_1 -> {organizador_1.obtenerEventos()}") # Mostramos los eventos de organizador_1, son 2
        print(f"Eventos de organizador_2 -> {organizador_2.obtenerEventos()}") # Mientras que los de organizador_2 son 0
        
        print(f"Eventos a los que va {part_1.obtenerNombre()}->",part_1.obtenerEventos()) # Mostramos los eventos de part_1
        
if __name__ == '__main__':
    Tester.runtest()