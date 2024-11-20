from Models.Entities.prestamo import Prestamo
import json

class RepoPrestamo:
    
    PATH = "Data/prestamos.json"
    
    def __init__(self):
        self.prestamos: list['Prestamo'] = self.cargarPrestamos()
    
    def cargarPrestamos(self):
        lista: list['Prestamo'] = []
        try:
            with open(RepoPrestamo.PATH, 'r') as file:
                prestamos_data = json.load(file)
                for prestamo in prestamos_data:
                    lista.append(Prestamo.fromDict(prestamo))
                
        except FileNotFoundError:
            print('No se encontró el archivo')
        
        Prestamo.establecerUltimoId(max([prestamo.getId() for prestamo in lista], default=0))
            
        return lista
    
    def guardarPrestamos(self):
        try:
            lista = [prestamo.toDict() for prestamo in self.prestamos]
            
            with open(RepoPrestamo.PATH, 'w') as file:
                json.dump(lista, file, indent=4)          
                
        except FileNotFoundError:
            print('No se encontró el archivo')
            
        Prestamo.establecerUltimoId(max([prestamo.getId() for prestamo in self.prestamos], default=0))
        
    def getPrestamos(self)->list['Prestamo']:
        return self.prestamos
    
    def getPrestamo(self, id: int)->Prestamo:
        for prestamo in self.prestamos:
            if prestamo.getId() == id:
                return prestamo
    
    def existe(self,socio_dni: int, libro_isbn:str, fecha_retiro:str)->bool:
        for prestamo in self.prestamos:
            if prestamo.getSocioDni() == socio_dni and prestamo.getLibroIsbn() == libro_isbn and prestamo.getFecha() == fecha_retiro:
                return True
        return False

    def estaDevuelto(self, prestamo: 'Prestamo')->bool:
        return prestamo.getFechaDevolucion() != None
    
    def agregarPrestamo(self, prestamo: 'Prestamo'):
        
        self.prestamos.append(prestamo)
        self.guardarPrestamos()
        
    def eliminarPorID(self, id: int)->bool:
        for prestamo in self.prestamos:
            if prestamo.getId() == id:
                self.prestamos.remove(prestamo)
                self.guardarPrestamos()
                return True
        return False
    
    def modificarPorID(self, id: int, socio_dni: int,libro_isbn:str, fecha_retiro:str, cant_dias:int ,fecha_devolucion:str):
        for prestamo in self.prestamos:
            if prestamo.getId() == id:
                prestamo.setSocioDni(socio_dni)
                prestamo.setLibroIsbn(libro_isbn)
                prestamo.setFechaRetiro(fecha_retiro)
                prestamo.setCantDias(cant_dias)
                prestamo.setFechaDevolucion(fecha_devolucion)
                self.guardarPrestamos()
                return True
        return False
    
    def cantidadLibrosSinDevolver(self, isbn:str)->int:
        cantidad = 0
        for prestamo in self.prestamos:
            if prestamo.getLibroISBN() == isbn and not self.estaDevuelto(prestamo):
                cantidad += 1
        return cantidad