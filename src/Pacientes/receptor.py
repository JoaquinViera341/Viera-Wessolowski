from paciente import paciente
from datetime import date

class receptor (paciente):

    def __init__(self, nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud, organo : str, fecha_inscripcion : date, prioridad : int, patologia : str, estable : bool):
        super().__init__(nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud)

        self.organo = organo

        self.fecha_inscripcion = fecha_inscripcion

        self.prioridad = prioridad

        self.patologia = patologia

        self.estable = estable #si el paciente esta estable es True , si esta inestable es false

        pass