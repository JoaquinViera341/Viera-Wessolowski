from Cirujano.cirujano import cirujano
from Vehiculos.vehiculo import vehiculos

class centro_salud(vehiculos, cirujano):
    
    def __init__(self, nombre : str, ciudad : str, povincia : str, direccion : str, telefono : int, lista_ciujanos : list,lista_vehiculos : list):

        self.nombre = nombre

        self.ciudad = ciudad

        self.provincia = povincia

        self.telefono = telefono

        self.lista_cirujanos = lista_ciujanos

        self.lista_vehiculos = lista_vehiculos

        self.direccion = direccion

        pass

    def agregar_cirujano(self, cirujano : cirujano):
        self.lista_cirujanos.append(cirujano)
        return self.lista_cirujanos
    
    def eliminar_cirujano (self, cirujano : cirujano):
        self.lista_cirujanos.remove(cirujano)
        return self.lista_cirujanos
    
    def agregar_vehiculo(self, vehiculo : vehiculos):
        self.lista_vehiculos.append(vehiculo)
        return self.lista_vehiculos
    
    def eliminar_vehiculo(self, vehiculo : vehiculos):
        self.lista_vehiculos.remove(vehiculo)
        return self.lista_vehiculos

        
        
