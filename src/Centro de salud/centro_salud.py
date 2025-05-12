from src.Cirujano.cirujano import cirujano
from src.Vehiculos.vehiculo import vehiculos

class centro_salud(vehiculos, cirujano):
    
    def __init__(self, nombre : str, ciudad : str, povincia : str, telefono : int, lista_ciujanos : list,lista_vehiculos : list):

        self.nombre = nombre

        self.ciudad = ciudad

        self.provincia = povincia

        self.telefono = telefono

        self.lista_cirujanos = lista_ciujanos

        self.lista_vehiculos = lista_vehiculos

        pass