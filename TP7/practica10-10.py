from abc import ABC, abstractmethod
from fecha import Fecha

class Producto(ABC):
    
    def __init__(self,id: int,precio: float):
        if not isinstance(id,int):
            raise ValueError("El id debe ser un entero")
        if not isinstance(precio,float):
            raise ValueError("El precio debe ser un flotante")
        
        self._id = id
        self._precio = precio
        
    def __str__(self):
        return f"ID: {self._id} Precio: {self._precio}"
    
    @abstractmethod
    def vender(self):
        pass
    
    @abstractmethod
    def sePuedeVender(self,cantidad:int):
        pass
    
    def obtenerId(self):
        return self._id
    
    def obtenerPrecio(self):
        return self._precio
    


class Juego(Producto):
   
    def __init__(self,id:int,precio:float,nombre:str, genero:str, anioLanzamiento:int, descripcion: str, modoOnline:bool):
        super().__init__(id,precio)
        
        if not isinstance(nombre,str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string")
        if not isinstance(genero,str):
            raise ValueError("El genero debe ser un string")
        if not isinstance(anioLanzamiento,int):
            raise ValueError("El año de lanzamiento debe ser un entero")
        if not isinstance(descripcion,str):
            raise ValueError("La descripcion debe ser un string")
        if not isinstance(modoOnline,bool):
            raise ValueError("El modo online debe ser un booleano")
        
        self._nombre = nombre
        self._genero = genero
        self._anioLanzamiento = anioLanzamiento
        self._descripcion = descripcion
        self._modoOnline = modoOnline
        
    
    def __str__(self):
        return super().__str__() +f"Nombre: {self._nombre} Genero: {self._genero} Año de lanzamiento: {self._anioLanzamiento} Descripcion: {self._descripcion} Modo Online: {self._modoOnline}"
    
    def __repr__(self):
        return f"{self._nombre}"
     
        
    def obtenerConsolasCompatibles(self):
        return self._listaConsolasCompatibles
    
    def obtenerCodigo(self):
        return self._codigo
    
    def obtenerNombre(self):
        return self._nombre
    
    def obtenerGenero(self):
        return self._genero
    
    def obtenerModoOnline(self):
        return self._modoOnline
    
    def agregarConsolaCompatible(self, consola:'Consola'):
        if not isinstance(consola,Consola):
            raise ValueError("El objeto no es una consola")
        self._listaConsolasCompatibles.append(consola)
        
    def quitarConsolaCompatible(self, consola:'Consola'):
        if not isinstance(consola,Consola):
            raise ValueError("El objeto no es una consola")
        self._listaConsolasCompatibles.remove(consola)
        
    # Comandos
    
    def establecerNombre(self, nombre:str):
        self._nombre = nombre
        
    def establecerGenero(self, genero:str):
        self._genero = genero
        
    def establecerAnioLanzamiento(self, anioLanzamiento:int):
        self._anioLanzamiento = anioLanzamiento
        
    def establecerDescripcion(self, descripcion:str):
        self._descripcion = descripcion
        
    def establecerModoOnline(self, modoOnline:bool):
        self._modoOnline = modoOnline
        
    # Consultas
    
    def obtenerNombre(self):
        return self._nombre
    
    def obtenerGenero(self):
        return self._genero
    
    def obtenerAnioLanzamiento(self):
        return self._anioLanzamiento
    
    def obtenerDescripcion(self):
        return self._descripcion
    
    def obtenerModoOnline(self):
        return self._modoOnline
    
    def obtenerCodigo(self):
        return self._codigo
        
       
        
        
class JuegoDigital(Juego):
    def __init__(self, id:int, precio:float, nombre:str, genero:str, anioLanzamiento:int, descripcion:str, modoOnline:bool, distribuidora:str,plataforma:str,tamanio:float):
        super().__init__(id, precio, nombre, genero, anioLanzamiento, descripcion, modoOnline)
        if not isinstance(distribuidora,str):
            raise ValueError("La distribuidora debe ser un string")
        if not isinstance(plataforma,str):
            raise ValueError("La plataforma debe ser un string")
        if not isinstance(tamanio,float):
            raise ValueError("El tamaño debe ser un flotante")
        
        self.__distribuidora = distribuidora
        self.__plataforma = plataforma
        self.__tamanio = tamanio
     
    def __str__(self):
        return super().__str__() + f" Distribuidora: {self.__distribuidora} Plataforma: {self.__plataforma} Tamaño: {self.__tamanio}"
    
    def __repr__(self):
        return f"{self._nombre}"
    # Comandos
    def vender(self, cantidad:int):
        if not isinstance(cantidad,int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero")
    
    # Consultas 
    
    def obtenerPlataforma(self):
        return self.__plataforma
    
    def obtenerDistribuidora(self):
        return self.__distribuidora
    
    def obtenerTamanio(self):
        return self.__tamanio
    
    def sePuedeVender(self, cantidad):
        return True
        
class JuegoFisico(Juego):
    def __init__(self,id:int,precio:float,nombre:str, genero:str, anioLanzamiento:int, descripcion: str, modoOnline:bool, stock:int):
        super().__init__(id,precio,nombre,genero,anioLanzamiento,descripcion,modoOnline)
        if not isinstance(stock,int) or stock <= 0:
            raise ValueError("El stock debe ser un entero")
        self.__stock = stock

    def __str__(self):
        return super().__str__() + f" Stock: {self.__stock}"
    
    def __repr__(self):
        return f"{self._nombre}"
    def obtenerStock(self):
        return self.__stock
    
    def establecerStock(self, stock:int):
        if not isinstance(stock,int) or stock <= 0:
            raise ValueError("El stock debe ser un entero")
        self.__stock = stock
        
    def agregarStock(self, cantidad:int):
        if not isinstance(cantidad,int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero")
        self.__stock += cantidad
    
    def vender(self, cantidad:int):
        if not isinstance(cantidad,int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero")
        if not self.sePuedeVender(cantidad):
            raise ValueError("No hay stock suficiente")
        
        self.__stock -= cantidad
        
    def sePuedeVender(self, cantidad):
        return self.__stock >= cantidad
        
class Consola(Producto):
    def __init__(self,id:int,precio:float,marca:str,modelo:str,almacenamiento:float,cantJoysticks:int,stock:int):
        super().__init__(id,precio)
        if not isinstance(marca,str):
            raise ValueError("La marca debe ser un string")
        if not isinstance(modelo,str):
            raise ValueError("El modelo debe ser un string")
        if not isinstance(almacenamiento,float):
            raise ValueError("El almacenamiento debe ser un flotante o un int")
        if not isinstance(cantJoysticks,int):
            raise ValueError("La cantidad de joysticks debe ser un entero")
        if not isinstance(stock,int):
            raise ValueError("El stock debe ser un entero")
        
        self.__marca = marca
        self.__modelo = modelo
        self.__almacenamiento = almacenamiento
        self.__cantJoysticks = cantJoysticks
        self.__stock = stock
        self.__listaJuegosCompatibles = []
    
    def __str__(self):
        return super().__str__()

    # Consultas
    
    def obtenerMarca(self):
        return self.__marca
    
    def obtenerModelo(self):
        return self.__modelo
    
    def obtenerAlmacenamiento(self):
        return self.__almacenamiento
    
    def obtenerCantJoysticks(self):
        return self.__cantJoysticks
    
    def obtenerStock(self):
        return self.__stock
    
    def obtenerJuegosCompatibles(self):
        return self.__listaJuegosCompatibles
    
    def establecerStock(self, stock:int):
        if not isinstance(stock,int) or stock <= 0:
            raise ValueError("El stock debe ser un entero")
        self.__stock = stock
        
    def agregarStock(self, cantidad:int):
        if not isinstance(cantidad,int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero")
        self.__stock += cantidad
        
    def agregarJuegoCompatible(self, juego:'Juego'):
        if not isinstance(juego,Juego):
            raise ValueError("El objeto no es un juego")
        self.__listaJuegosCompatibles.append(juego)
        
    def quitarJuegoCompatible(self, juego:'Juego'):
        if not isinstance(juego,Juego):
            raise ValueError("El objeto no es un juego")
        self.__listaJuegosCompatibles.remove(juego)
        
    def sePuedeVender(self, cantidad):
        return self.__stock >= cantidad
    
    def vender(self, cantidad:int):
        if not isinstance(cantidad,int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero")
        if not self.sePuedeVender(cantidad):
            raise ValueError("No hay stock suficiente")
        
        self.__stock -= cantidad
        
class Cliente:
    def __init__(self,nombre:str,apellido:str,dni:int,mail:str):
        if not isinstance(nombre,str):
            raise ValueError("El nombre debe ser un string")
        if not isinstance(apellido,str):
            raise ValueError("El apellido debe ser un string")
        if not isinstance(dni,int):
            raise ValueError("El dni debe ser un entero")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__mail = mail
    
    def __str__(self):
        return f"Nombre: {self.__nombre} Apellido: {self.__apellido} DNI: {self.__dni} MAIL {self.__mail}"
    def comprar(self):  
        pass
       
class Compra:
    def __init__(self,cliente:'Cliente',fecha:'Fecha',formaPago:str):
        if not isinstance(fecha,Fecha):
            raise ValueError("La fecha debe ser un objeto de la clase Fecha")
        if not isinstance(formaPago,str):
            raise ValueError("La forma de pago debe ser un string")
        if not isinstance(cliente,Cliente):
            raise ValueError("El cliente debe ser un objeto de la clase Cliente")
        
        self.__fecha = fecha
        self.__formaPago = formaPago
        self.__estado = "Pendiente"
        self.__listaItems:list[Item] = []
        self.__cliente = cliente
        
    def __str__(self):
        return f"Fecha: {self.__fecha} Forma de pago: {self.__formaPago} Estado: {self.__estado} Cliente: {self.__cliente} \n Items: {self.__listaItems}"
    def obtenerFecha(self):
        return self.__fecha
    
    def obtenerFormaPago(self):
        return self.__formaPago
    
    def obtenerEstado(self):
        return self.__estado
    
    def obtenerCliente(self):
        return self.__cliente
    
    def obtenerItems(self):
        return self.__listaItems
    
        
    def agregarItem(self,item:'Item'):
        if not isinstance(item,Item):
            raise ValueError("El item debe ser un objeto de la clase Items")
        self.__listaItems.append(item)
    
    def entregar(self):
        self.__estado = "Entregado"

    def costoTotal(self):
        total = 0
        for item in self.__listaItems:
            total += item.obtenerProducto().obtenerPrecio() * item.obtenerCantidad()
        return total
    
class Item:
    def __init__(self,producto:'Producto',cantidad:int=1):
        if not isinstance(producto,Producto):
            raise ValueError("El producto debe ser un objeto de la clase Producto")
        if not isinstance(cantidad,int):
            raise ValueError("La cantidad debe ser un entero")
        
        self.__producto = producto
        self.__cantidad = cantidad
    
    def __str__(self):
        return f"Producto: {self.__producto} Cantidad: {self.__cantidad}"
    
    def __repr__(self):
        return f"{self.__producto} Cantidad: {self.__cantidad}"
    
    def obtenerProducto(self):
        return self.__producto
    
    def obtenerCantidad(self):
        return self.__cantidad
    
    
    
class Tester:
    @staticmethod
    def run():
        consola_1 = Consola(1,1000000.0,"Sony","Playstation 5",825.0,1,10)
        print(consola_1)
        juego_1 = JuegoDigital(2,5000.0,"The Last of Us Part II","Aventura",2020,"Juego de aventura en tercera persona",False,"Sony","Playstation 4",100.0)
        juego_2 = JuegoFisico(3,3000.0,"Uncharted","Aventura",2016,"Juego de aventura en tercera persona",False,15)
     
        print(juego_1)
        print(juego_2)   
        consola_1.agregarJuegoCompatible(juego_1) # agregar juego compatible
        consola_1.agregarJuegoCompatible(juego_2) # agregar juego compatible
        print(consola_1.obtenerJuegosCompatibles()) # obtener juegos compatibles
        consola_1.quitarJuegoCompatible(juego_1)
        print(consola_1.obtenerJuegosCompatibles())
        
        
        cliente_1 = Cliente("Juan","Perez",123456789,"juanperez@gmail.com")
        print(cliente_1)
        
        item_1 = Item(juego_1,1)
        item_2 = Item(juego_2,1)
        compra_1 = Compra(cliente_1,Fecha.obtenerFechaActual(),"Efectivo")
        compra_1.agregarItem(item_1)
        compra_1.agregarItem(item_2)
        print(compra_1)
        compra_1.entregar()
        
if __name__ == "__main__":
    Tester.run()