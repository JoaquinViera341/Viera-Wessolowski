from datetime import date

class paciente():

    def __init__(self, nombre : str, dni : int, fecha_nacimiento : date, sexo : str, telefono_contacto : int, tipo_sangre : str, centro_salud : str ) :
        
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono_contacto = telefono_contacto
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud




    
         
        