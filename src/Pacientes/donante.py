from Pacientes.paciente import paciente
from datetime import datetime

class donante (paciente) :

    def __init__(self, nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud, fecha_hora_fallecimiento : datetime, lista_organos : list, lista_fecha_organo_ablacion : list):
        super().__init__(nombre, DNI, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud)



        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento

        self.lista_organos = lista_organos

        self.lista_fecha_organo_ablacion = lista_fecha_organo_ablacion



####################################################################################################################################################################


    # METODOS MAGICOS :



    def __str__(self) -> str :
        """ Este metodo lo que hace es dar una pequeña presentacion de un objeto donante  """

        list_organo = ", ".join(self.lista_organos)

        if self.lista_fecha_organo_ablacion:
            list_fecha_ablacion = ", ".join(str(item) for item in self.lista_fecha_organo_ablacion) #los convierto a todos en str para que no haya errores
        else:
            list_fecha_ablacion = "Aun no se ha realizado ninguna ablacion"
        
        if self.fecha_hora_fallecimiento: #En este caso es si el donante ya fallecio
            text = (
                f"Nombre: {self.nombre} \n"
                f"DNI: {self.dni} \n"
                f"Fecha de nacimiento: {self.fecha_nacimiento} \n"
                f"Sexo: {self.sexo} \n"
                f"Telefono: {self.telefono_contacto} \n"
                f"Tipo de sangre: {self.tipo_sangre} \n"
                f"Centro de salud: {self.centro_salud} \n"
                f"Fecha fallecimiento: {self.fecha_hora_fallecimiento} \n"
                f"Lista de organos disponibles: {list_organo} \n"
                f"Lista de fechas de ablacion: {list_fecha_ablacion}"
            )
        elif not self.fecha_hora_fallecimiento: # En este caso es si sigue vivo
            text = (
                f"Nombre: {self.nombre} \n"
                f"DNI: {self.dni} \n"
                f"Fecha de nacimiento: {self.fecha_nacimiento} \n"
                f"Sexo: {self.sexo} \n"
                f"Telefono: {self.telefono_contacto} \n"
                f"Tipo de sangre: {self.tipo_sangre} \n"
                f"Centro de salud: {self.centro_salud} \n"
                f"Lista de organos disponibles: {list_organo} \n"
                f"Lista de fechas de ablacion: {list_fecha_ablacion}"
            )
        return text




    def __eq__(self , otro ) -> None :

        """ Este metodo lo que hace es comparar dos objetos , devuelve true si los objetos son de tipo donante   , y tiene el mismo DNI , es decir son iguales   """

        return isinstance(otro , donante ) and self.DNI == otro.DNI
    




    def __len__(self) -> int :

        """ Este metodo lo que hace es contar la cantidad de organos que tiene el donante para donar """

        return len(self.lista_organos)

    



#####################################################################################################################################################################





    def eliminar_organo(self , organo : int) -> list  :



        """ Este metodo se encarga de eliminar un organo de la lista de organos disponibles y registrar su ablacion con fecha y hora """
        

        hora = datetime.now() 
        

        text = f"Organo: {self.lista_organos[organo]} Dia: {hora.strftime('%d/%m/%Y %H:%M:%S')}" 


        self.lista_fecha_organo_ablacion.append(text) # añado el organo y la fecha de ablacion a la lista de ablacion
      

        self.lista_organos.pop(organo) 


        return self.lista_organos, self.lista_fecha_organo_ablacion # devuelvo la lista de organos y la lista de fechas de ablacion actualizadas 





######################################################################################################################################################################





    def agregar_fecha_muerte(self, fecha_fallecimiento : datetime, lista_organos : list) -> datetime :


        """ Este metodo  registra la fecha y hora del fallecimiento del donante y vacía la lista de órganos disponibles """


        self.fecha_hora_fallecimiento = fecha_fallecimiento 

        self.lista_organos = lista_organos 

        return self.fecha_hora_fallecimiento
    



#######################################################################################################################################################################




    def actualizar_lista_ablacion(self, organo : int)->None :

        """Añado los organos que se quitaron a la lista"""

        self.lista_fecha_organo_ablacion.append("Organo:", self.lista_organos[organo], "Fecha:", datetime.now)
        self.lista_organos.pop(organo)

        return None