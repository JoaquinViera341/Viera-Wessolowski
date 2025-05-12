from abc import ABC, abstractclassmethod 
import googlemaps as gmaps

gmaps_key

class vehiculos (ABC):

    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):

        self.velocidad = velocidad

        self.lista_viajes = lista_viajes

        self.disponibilidad = disponibilidad #si el vehiculo esta disponible es True , si no es false

        pass

class auto(vehiculos):
    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass

class avion(vehiculos):
    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass

class helicoptero(vehiculos):
    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass