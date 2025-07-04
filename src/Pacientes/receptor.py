from Pacientes.paciente import paciente
from datetime import datetime

class receptor (paciente):

    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud, organo : str, fecha_inscripcion : datetime , prioridad : int , patologia : str , estable : bool ) :
        
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono_contacto, tipo_sangre, centro_salud)

        self.organo = organo
        self.fecha_inscripcion = fecha_inscripcion
        self.prioridad = prioridad
        self.patologia = patologia
        self.estable = estable



    # METODOS MAGICOS :

    def __str__(self) -> str :


        """ Este metodo lo que hace es dar una pequeña presentacion de un objeto receptor  """


        if self.estable == True : 
            estado = "Estable"

        else:
            estado = "Inestable"
        
        text = (
            f"Nombre: {self.nombre} \n"
            f"DNI: {self.dni} \n"
            f"Fecha de nacimiento: {self.fecha_nacimiento} \n"
            f"Sexo: {self.sexo} \n"
            f"Telefono: {self.telefono_contacto} \n"
            f"Tipo de sangre: {self.tipo_sangre} \n"
            f"Centro de salud: {self.centro_salud} \n"
            f"Organos requeridos: {self.organo} \n"
            f"Fecha de inscripcion: {self.fecha_inscripcion} \n"
            f"Prioridad: {self.prioridad} \n"
            f"Patologia: {self.patologia} \n"
            f"Estado del paciente : {estado}"
        )
        
        return text



    def __eq__(self , otro ) -> None :

        """ Este metodo lo que hace es comparar dos objetos , devuelve true si los objetos son de tipo receptor  , y tiene el mismo DNI , es decir son iguales   """

        return isinstance(otro , receptor ) and super().DNI == super().DNI
    




    def __bool__(self) -> bool :

        """ Este metodo magico devuelve la estabilidad de un receptor para recibir un organo """
        
        return self.estable





    def cambiar_prioridad(self) -> int :


        """ Este metoo lo que hace es cambiar la prioridad del paciente , que en este caso seria la de un receptor """
        
        self.prioridad = 10

        return self.prioridad


    
    def cambiar_estable(self, nuevo_estado : bool) -> bool :

        """ Este metodo metodo lo que hace es cambiar el estado del paciente """

        if self.estable == True :
            self.estable = False
            return self.estable