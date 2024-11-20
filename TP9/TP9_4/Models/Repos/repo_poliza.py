from Models.Entities.poliza_inmueble import PolizaInmueble
from Models.Entities.poliza_inmueble_escolar import PolizaInmuebleEscolar

import json

class RepoPoliza:
    PATH = 'Data/polizas.json'
    
    def __init__(self):
        self.polizas:list['PolizaInmueble'] = self.cargarPolizas()
        
    def cargarPolizas(self)->list['PolizaInmueble']:
        lista = []
        try:
            with open(RepoPoliza.PATH, 'r') as file:
                polizas_data = json.load(file)
                for poliza in polizas_data:
                    if not 'cantPersonas' in poliza: # si no tiene el campo cantPersonas es una poliza normal
                        lista.append(PolizaInmueble.fromDict(poliza))
                    else :
                        lista.append(PolizaInmuebleEscolar.fromDict(poliza))
        
        except FileNotFoundError:
            print('No se encontró el archivo')
        
        return lista
    
    def guardarTodas(self):
        try:
            lista = [poliza.toDict() for poliza in self.polizas]
            
            with open(RepoPoliza.PATH, 'w') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print('No se encontró el archivo')
            
    def getPolizas(self)->list:
        return self.polizas
    
    def getPoliza(self, numero:int):
        for poliza in self.polizas:
            if poliza.getNumero() == numero:
                return poliza
    
    def existe(self, otraPoliza):
        for poliza in self.polizas:
            if poliza.getNumero() == otraPoliza.getNumero():
                return True
        return False
    
    def existeNumero(self, numero:int):
        for poliza in self.polizas:
            if poliza.getNumero() == numero:
                return True
        return False
    
    def agregarPoliza(self, nuevaPoliza):
        if not isinstance(nuevaPoliza, PolizaInmueble) and not isinstance(nuevaPoliza, PolizaInmuebleEscolar):
            raise ValueError('El objeto no es una poliza')
        if self.existe(nuevaPoliza):
            raise ValueError('La poliza ya existe')
        
        self.polizas.append(nuevaPoliza)
        self.guardarTodas()

    
    def eliminarPoliza(self, numero:int):
        for poliza in self.polizas:
            if poliza.getNumero() == numero:
                self.polizas.remove(poliza)
                self.guardarTodas()
                return True
        return False
    
    def modificarPorNumero(self,numero:int,incendio:float,explosion:float,robo:float,cantPersonas:int=None,montoEquipamiento:float=None,montoInmobiliario:float=None,montoPersona:float=None):
        for poliza in self.polizas:
            if poliza.getNumero() == numero:
                poliza.setIncendio(incendio)
                poliza.setExplosion(explosion)
                poliza.setRobo(robo)
                
                if cantPersonas is not None and isinstance(poliza, PolizaInmuebleEscolar):
                    poliza.setCantPersonas(cantPersonas)
                    poliza.setMontoEquipamiento(montoEquipamiento)
                    poliza.setMontoInmobiliario(montoInmobiliario)
                    poliza.setMontoPersona(montoPersona)
                self.guardarTodas()
                return True
        return False
                
                
                