import datetime as dt
import json

class PaqueteGrupal:
    
    TIPOS_VIAJES = ['Turismo','Educativo','Aventura']
    
    def __init__(self,id_paquete:int,ciudad:'Ciudad',fecha_ida:dt.date,fecha_Vuelta:dt.date,descripcion:str,tipo_viaje:str,precio: int | float, cupo_maximo:int,cupo_actual:int=0):
        pass
    
    def __str__(self):
        pass
    

class Ciudad:
    
    def __init__(self,nombre:str,provincia:str,puntos_interes:list[str]):
        pass
    
    def __str__(self):
        pass
    
class Hotel:
    
    TIPOS_PENSION = ['Desayuno','Media Pension','Pension Completa']
    
    def __init__(self,nombre:str,ciudad:'Ciudad',descripcion:str,estrellas:int,tipo:str):
        pass
    
    def __str__(self):
        pass
    
    @classmethod
    def from_json(cls,nombre:str,nombre_ciudad:str):
        with open("hoteles.json","r") as file:
            hoteles = json.load(file)
            for hotel in hoteles:
                if hotel['nombre'].lower() == nombre.lower() and hotel['ciudad'].lower() == nombre_ciudad.lower():
                    return cls()
class Transporte:
    
    TIPOS_TRANSPORTE = ['Aereo','Terrestre','Maritimo']
    
    def __init__(self,tipo:str):
        pass
    
    
if __name__ == "__main__":
    
    pass
