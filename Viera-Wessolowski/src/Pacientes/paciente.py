from datetime import datetime , date , time

class paciente():

    def __init__(self, nombre : str, DNI : int, fecha_nacimiento : datetime, sexo : str, telefono_contacto : int, tipo_sangre : str, centro_salud : any ):
        self.nombre = nombre
        
        self.DNI = DNI

        self.fecha_nacimiento = fecha_nacimiento

        self.sexo = sexo

        self.telefono_contacto = telefono_contacto

        self.tipo_sangre = tipo_sangre

        self.centro_salud = centro_salud

        pass