from paciente import paciente
from datetime import datetime
from paciente import paciente



class donante (paciente):



    def _init_(self, nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud, fecha_hora_fallecimiento : datetime , lista_organos : list , lista_fecha_organo_ablacion : datetime ) :


        super()._init_(nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud)


        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento


        self.lista_organos = lista_organos


        self.lista_fecha_organo_ablacion = lista_fecha_organo_ablacion





    def Presentacion_donante(self) :


        # devuelve un string con los datos del donante

        return super().__str__ + f" Organos disponibles  para donar : {self.lista_organos} "
    




    def Eliminar_organo(self , organo : str ) :


        # Elimino un organo de la lista de disponibilidad 


        if organo in self.lista_organos : # Si el organo esta en la lista de organos disponibles

            self.lista_organos.remove(organo)  
            self.lista_fecha_organo_ablacion.append(datetime.now()) # Agrego la fecha de ablacion del organo a la lista de fechas de ablacion


            print("El organo ha sido eliminado de la lista de organos disponibles")

            
        
        else : # Si el organo no esta en la lista de organos disponibles


            print("El organo no esta en la lista de organos disponibles")



        

     


    