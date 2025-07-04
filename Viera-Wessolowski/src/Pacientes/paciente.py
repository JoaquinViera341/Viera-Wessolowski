from abc import ABC, abstractmethod
from datetime import date


class paciente(ABC):

    def _init_(self, nombre : str, DNI : int, fecha_nacimiento : date , sexo : str, telefono_contacto : int, tipo_sangre : str, centro_salud : any ):
        
        
        self.nombre = nombre
        
        self.DNI = DNI

        self.fecha_nacimiento = fecha_nacimiento

        self.sexo = sexo

        self.telefono_contacto = telefono_contacto

        self.tipo_sangre = tipo_sangre

        self.centro_salud = centro_salud



    def __str__(self) :

        # Devuelve un string con los datos no completos del paciente


        return f"Nombre: {self.nombre}, DNI: {self.DNI}, Fecha de nacimiento: {self.fecha_nacimiento} "