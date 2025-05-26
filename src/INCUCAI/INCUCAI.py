from Centro_de_salud import centro_salud
from Pacientes.donante import donante
from Pacientes.receptor import receptor

class INCUCAI (centro_salud , donante , receptor) :


    def __init__(self, centro_salud : list, lista_donantes : donante, lista_receptores : receptor ) :

        self.centro_salud = centro_salud
        
        self.lista_donantes = lista_donantes
        
        self.lista_receptores = lista_receptores

        pass


    def guardar_centro_salud(self, centro_salud : centro_salud):
        self.centro_salud.append(centro_salud)
        return self.centro_salud
    
    def match_donante (self, donante:donante):
        lista_aux_1 = []
        receptor_aux = receptor()

        for x in len(self.lista_receptores):
            if donante.tipo_sangre == self.lista_receptores[x].tipo_sangre:
                for y in len(donante.lista_organos):
                    if donante.lista_organos[y] == self.lista_receptores[x].organo:
                        lista_aux_1.append(self.lista_receptores[x])
        if len(lista_aux_1) == 0:
            return False
        elif len(lista_aux_1) == 1:
            return lista_aux_1[0]
        else:
            receptor_aux = lista_aux_1[0]
            for i in len(lista_aux_1):
                if receptor_aux.prioridad < lista_aux_1[i].prioridad:
                    receptor_aux = lista_aux_1[i]
            return receptor_aux
        
    def match_receptor (self, receptor:receptor):
        for x in len(self.lista_donantes):
            if receptor.tipo_sangre == self.lista_donantes[x].tipo_sangre:
                for y in len(self.lista_donantes[x].lista_organos):
                    if self.lista_donantes[x].lista_organos[y] == receptor.organo:
                        return self.lista_donantes[x]
        return False