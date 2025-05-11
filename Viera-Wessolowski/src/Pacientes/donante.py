from paciente import paciente
from datetime import datetime

class donante (paciente):

    def __init__(self, nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud, fecha_hora_fallecimiento : datetime, lista_organos : list, lista_fecha_organo_ablacion : datetime):
        super().__init__(nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud)

        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento

        self.lista_organos = lista_organos

        self.lista_fecha_organo_ablacion = lista_fecha_organo_ablacions