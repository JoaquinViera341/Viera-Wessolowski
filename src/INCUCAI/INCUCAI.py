from centro_salud import centro_salud
from Pacientes.donante import donante
from Pacientes.receptor import receptor

class INCUCAI (centro_salud, donante, receptor):


    def __init__(self, centro_salud : list, lista_donantes : list, lista_receptores : list):
        self.centro_salud = centro_salud
        
        self.lista_donantes = lista_donantes
        
        self.lista_receptores = lista_receptores

        pass