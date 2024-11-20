from Models.Entities.socio import Socio
import json
import datetime

class RepoSocio:
    PATH = 'Data/socios.json'
    
    def __init__(self):
        self.socios: list['Socio'] = self.cargarSocios()

    def cargarSocios(self) -> list['Socio']:
        lista: list['Socio'] = []
        try:
            with open(RepoSocio.PATH, 'r') as file:
                socios_data = json.load(file)
                for socio in socios_data:
                    lista.append(Socio.fromDict(socio))
        except FileNotFoundError:
            print('No se encontró el archivo de socios')
            
        return lista
    
    def guardarSocios(self):
        try:
            lista = [socio.toDict() for socio in self.socios]
            
            with open(RepoSocio.PATH, 'w') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print('No se encontró el archivo de socios')
            
    def getSocios(self)->list['Socio']:
        return self.socios
    
    def getSocio(self, dni: str)->Socio:
        for socio in self.socios:
            if socio.getDni() == dni:
                return socio
            
    def existe(self,socio: Socio)->bool:
        for socio in self.socios:
            if socio.getDni() == socio.getDni():
                return True
        return False
    
    def existeDNI(self,dni: str)->bool:
        for socio in self.socios:
            if socio.getDni() == dni:
                return True
        return False
    
    def agregarSocio(self, socio: Socio):
        self.socios.append(socio)
        self.guardarSocios()
        
    def eliminarPorDNI(self, dni: str)->bool:
        for socio in self.socios:
            if socio.getDni() == dni:
                self.socios.remove(socio)
                self.guardarSocios()
                return True
        return False
    
    def modificarSocio(self, dni: str, nombre: str, apellido: str, mail: str, fechaNac: str)->bool:
        for socio in self.socios:
            if socio.getDni() == dni:
                socio.setNombre(nombre)
                socio.setApellido(apellido)
                socio.setMail(mail)
                
                socio.setFechaNacimiento(fechaNac)
                self.guardarSocios()
                return True
        return False