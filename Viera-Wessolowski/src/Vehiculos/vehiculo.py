from abc import ABC, abstractclassmethod 

class vehiculos (ABC):

    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):

        self.velocidad = velocidad

        self.lista_viajes = lista_viajes

        self.disponibilidad = disponibilidad

        pass