from Cirujano.cirujano import cirujano
from Vehiculos.vehiculo import vehiculos, avion, auto, helicoptero
from typing import List
from typing import Optional
from typing import Union

class centro_salud():
    
    
    def __init__(self, nombre : str, partido : str, provincia : str, direccion : str, telefono : int, lista_cirujanos : List[cirujano],lista_aviones : List[avion], lista_ambulancias : List[auto], lista_helicopteros : List[helicoptero]):

        self.nombre = nombre
        self.partido = partido 
        self.provincia = provincia 
        self.telefono = telefono
        
        self.lista_cirujanos = lista_cirujanos if lista_cirujanos is not None else []
        self.lista_aviones = lista_aviones if lista_aviones is not None else []
        self.lista_ambulancias = lista_ambulancias if lista_ambulancias is not None else []
        self.lista_helicopteros = lista_helicopteros if lista_helicopteros is not None else []
        self.direccion = direccion


    # METODOS MAGICOS ...



    def __str__(self) -> str :


        """ Este metodo hace una presentacion basica del centro de salud """


        return f"Nombre : {self.nombre} \n Partido : {self.partido } \n Provincia : {self.provincia} \n Telefono : {self.telefono} \n direccion : {self.direccion}"



    def __len__(self) -> None :
 

        " Calcula la cantidad de cirujanos y vehiculos que hay en el centro de salud "


        print(f"El centro de salud tiene habilitados {len(self.lista_cirujanos)} cirujanos  y {len(self.lista_vehiculos)} vehiculos  ")



    def __iadd__(self , otros_cirujanos : list[cirujano] ) -> None :


        """ Este metodo agrega varios cirujanos a mi lista . se llama desde el main  con += """


        self.lista_cirujanos.extend(otros_cirujanos) 


    def menu_institucion(self) :

        while True :
            
            print("Bienvenido al menu del " + self.nombre)
            print("1. Imprimir cirujanos")
            print("2. Imprimir ambulancias")
            print("3. Imprimir helicopteros")
            print("4. Imprimir aviones")
            print("5. Agregar cirujano")
            print("6. Agregar ambulancia")
            print("7. Agregar helicoptero")
            print("8. Agregar avion")
            print("9. Eliminar cirujano")##
            print("10. Eliminar ambulancia")
            print("11. Eliminar helicoptero")
            print("12. Eliminar avion")
            print("13. Salir")
            print("\n")

            opcion = input("Ingresar una opcion:")

            if opcion == "1":
                self.imprimir_cirujanos()
            if opcion == "2":
                self.imprimir_ambulancias()
            if opcion == "3":
                self.imprimir_helicopteros()
            if opcion == "4":
                self.imprimir_aviones()
            if opcion == "5":
                self.agregar_cirujano()
            if opcion == "6" :
                self.agregar_ambulancia()
            if opcion == "7" :
                self.agregar_helicoptero()
            if opcion == "8" :
                self.agregar_avion()
            if opcion == "9" :
                self.eliminar_cirujano()
            if opcion == "10":
                self.eliminar_ambulancia()
            if opcion == "11":
                self.eliminar_helicoptero()
            if opcion == "12":
                self.eliminar_avion()
            

            if opcion == "13":
                print("Saliendo del menu del centro de salud")
                return None



####################################################################################################################################################################



    def imprimir_cirujanos(self) ->None:
        """ Este metodo imprime los cirujanos que hay en el centro de salud """

        for cirujano in self.lista_cirujanos:
            print(cirujano)
            print("----------------------------------")

    
    def imprimir_ambulancias(self) -> None:
        """ Este metodo imprime las ambulancias que hay en el centro de salud """

        for ambulancia in self.lista_ambulancias:
            print(ambulancia)
            print("----------------------------------")
        
    
    def imprimir_helicopteros(self) -> None:
        """ Este metodo imprime los helicopteros que hay en el centro de salud """

        for helicoptero in self.lista_helicopteros:
            print(helicoptero)
            print("----------------------------------")
        
    
    def imprimir_aviones(self) -> None:
        """ Este metodo imprime los aviones que hay en el centro de salud """

        for avion in self.lista_aviones:
            print(avion)
            print("----------------------------------")
        


####################################################################################################################################################################




    def agregar_cirujano(self) -> None :


        """Este metodo lo que hace es agregar un objeto cirujano a una lista de cirujanos que esta en la clase centro de salud """
        

        especialidades = ["Cardiologo", "Gastroenterologo", "Pulmonar", "Taumatologo", "Plastico"]


        print ("--Ingrese los datos del cirujano a agregar:")
        nombre = input("Nombre:")
        dni = int(input("DNI:"))


        print("A continuacion se mostraran las especialidades disponibles, ingrese el numero correspondiente")


        for indice_especialidades in range(len(especialidades)) :

            print(f"{indice_especialidades+1}. {especialidades[indice_especialidades]}\n")

        especialidad = input("Especialidad:")



        if especialidad <= 5 and especialidad >= 1:

            especialidad = especialidades[especialidad - 1]


        else:


            print("Especialidad no valida, intente de nuevo.")
            return None



        cirujano_nuevo = cirujano(dni , especialidad , True , nombre)
        self.lista_cirujanos.append(cirujano_nuevo)
        print ("Cirujano agregado correctamente")
        return None



####################################################################################################################################################################




    def agregar_ambulancia(self) -> None :


        """ Este metodo lo que haces es agregar un objeto ambulancia a una lista de ambulancias que esta en la clase centro de salud """


        print ("--Ingrese los datos de la ambulancia a agregar:")


        velocidad = input("Velocidad:")
        lista_viajes = list()
        lista_fecha_viajes = list() 
        disponibilidad = True 
        matricula = str(input("Matricula:"))



        for indice_ambulancia in range(len(self.lista_ambulancias)) :

            if self.lista_ambulancias[indice_ambulancia].matricula == matricula:

                print("La ambulancia ya existe , intente con otra matricula")
                return None
            

            

        ambulancia_nueva = auto(velocidad , lista_viajes , lista_fecha_viajes , disponibilidad , disponibilidad , matricula)
        self.lista_ambulancias.append(ambulancia_nueva)
        print ("Ambulancia agregada correctamente")
        return None





####################################################################################################################################################################





    def agregar_helicoptero(self) -> None :


        """ Este metodo lo que hace es agregar un objeto helicoptero a una lista de helicopteros que esta en la clase  centro de salud """
        

        print ("--Ingrese los datos del helicoptero a agregar:")

        velocidad  = input("Velocidad:")
        lista_viajes = list()
        lista_fecha_viajes = list()
        disponibilidad = True
        matricula = str(input("Matricula:"))

        for indice_helicoptero in range(len(self.lista_helicopteros)):

            if self.lista_helicopteros[indice_helicoptero].matricula == matricula:

                print("El helicoptero ya existe , intente con otra matricula")
                return None


            

        helicoptero_nuevo = helicoptero(velocidad,lista_viajes,lista_fecha_viajes,disponibilidad,matricula)
        self.lista_ambulancias.append(helicoptero_nuevo)
        print("Helicoptero agregado correctamente")
        return None





#####################################################################################################################################################################



    
    def agregar_avion(self)-> None :


        """ Este metodo lo que hace es agregar un objeto avion a una lista de aviones que esta en la clase centro de salud """


        print("--Ingrese los datos del avion a agregar:")


        velocidad = input("Velocidad:")
        lista_viajes = list()
        lista_fecha_viajes = list()
        disponibilidad = True
        matricula = str(input("Matricula:"))


        for indice_avion in range(len(self.lista_aviones)) :


            if self.lista_aviones[indice_avion].matricula == matricula:
                print("El avion ya existe , intente con otra matricula")
                return None




        avion_nuevo = avion(velocidad, lista_viajes, lista_fecha_viajes, disponibilidad, matricula)
        self.lista_ambulancias.append(avion_nuevo)
        print("Avion agregado correctamente")
        return None




   #########################################################################################################################################################################



    def eliminar_cirujano (self) -> None :



        """ Este metodo lo que hace es eliminar un cirujano de la lista de cirujanos que esta en la clase centro de salud  """


        dni = int(input("Ingrese el DNI del cirujano a eliminar: "))
        indice_cirujano = self.buscar_cirujano_por_dni(dni)


        if indice_cirujano is False :

            print("Cirujano no encontrado.")
            return None


        else :


            self.lista_ambulancias.pop(indice_cirujano)
            print("Cirujano eliminado correctamente por indice.")
            return None

        



    def buscar_cirujano_por_dni(self, dni : int) -> Union[int,bool] :

        """ Este metodo busca un cirujano por su dni y devuelve su indice en la lista de cirujanos """

        for indice_cirujano in range(len(self.lista_cirujanos)) :

            if self.lista_cirujanos[indice_cirujano].dni == dni :

                return indice_cirujano
            

            

            return False



#####################################################################################################################################################################




    def eliminar_ambulancia(self) -> None :

        """ Este metodo lo que hace es eliminar una ambulancia de la lista de ambulancias que esta en la clase centro de salud """

        matricula = str(input("Ingrese la matricula de la ambulancia a eliminar: "))
        
        indice_ambulancia = self.buscar_ambulancia_por_matricula(matricula)


        if indice_ambulancia is False :

            print("Ambulancia no encontrada.")
            return None

        
        else :


            self.lista_ambulancias.pop(indice_ambulancia)
            print("Ambulancia eliminada correctamente por indice.")
            return None


        
        


    def buscar_ambulancia_por_matricula(self, matricula : str) -> Union[int,bool]:

            """ Este metodo busca un transporte por su matricula y devuelve su indice en la lista de vehiculos """


            for indice_ambulancia in range(len(self.lista_ambulancias)) :

                if self.lista_ambulancias[indice_ambulancia].matricula == matricula :

                    return indice_ambulancia

                else :

                    return False  






######################################################################################################################################################################




    def eliminar_helicoptero(self) -> None :


        """ Este metodo lo que hace es eliminar un helicoptero de la lista de helicopteros que esta en la clase centro de salud """


        matricula = str(input("Ingrese la matricula del helicoptero a eliminar: "))
        
        indice_helicoptero = self.buscar_helicoptero_por_matricula(matricula)


        if indice_helicoptero is False :

            print("Helicoptero no encontrado.")
            return None


        else :


            self.lista_helicopteros.pop(indice_helicoptero)
            print("Helicoptero eliminado correctamente por indice.")
            return None




    def buscar_helicoptero_por_matricula(self, matricula : str) -> Union[int,bool] :


        """ Este metodo busca un helicoptero por su matricula y devuelve su indice en la lista de helicopteros """


        for indice_helicoptero in range(len(self.lista_helicopteros))  :

            if self.lista_helicopteros[indice_helicoptero].matricula == matricula :

                return indice_helicoptero

            else :

              
                return False




#######################################################################################################################################################################




    def eliminar_avion(self) -> None :


        """ Este metodo lo que hace es eliminar un avion de la lista de aviones que esta en la clase centro de salud """

        matricula = str(input("Ingrese la matricula del avion a eliminar: "))
        
        indice_avion = self.buscar_avion_por_matricula(matricula)


        if indice_avion is False :


            print("Avion no encontrado.")
            return None



        else :


            self.lista_aviones.pop(indice_avion)
            print("Avion eliminado correctamente por indice.")
            return None
        



        
       
    def buscar_avion_por_matricula(self, matricula : str) -> Union[int,bool] :

        """ Este metodo busca un avion por su matricula y devuelve su indice en la lista de aviones """


        for indice_avion in range(len(self.lista_aviones)) :


            if self.lista_aviones[indice_avion].matricula == matricula :


                return indice_avion


            else : 

                return False



        
########################################################################################################################################################################


    
    
    def reiniciar_disponibilidad(self) -> None :

        """Este metodo lo que hacer es recorrer la lista de cirujanos, y las de vehiculos y reiniciar su disponibilidad """


        for indice_cirujano in (1,len(self.lista_cirujanos)) :


            if self.lista_cirujanos [indice_cirujano].disponibilidad == False : 
                self.lista_cirujanos[indice_cirujano].disponibilidad == True



        for indice_ambulancia in (1,len(self.lista_ambulancias)) :    


            if self.lista_ambulancias[indice_ambulancia].disponibilidad == False :
                self.lista_ambulancias[indice_ambulancia].disponibilidad == True


        for indice_helicoptero in (1,len(self.lista_helicopteros)) :


            if self.lista_helicopteros[indice_helicoptero].disponibilidad == False : 
                self.lista_helicopteros[indice_helicoptero].disponibilidad == True


        for indice_avion in (1,len(self.aviones)) :


            if self.lista_aviones[indice_avion].disponibilidad == False : 
                self.lista_aviones[indice_avion].disponibilidad == True


#########################################################################################################################################################################



    def asignar_cirujano (self) -> int :


        """ Este metodo busca que cirujano esta disponible y lo envia a hacer la cirugia """


        for indice_cirujano in range(len(self.lista_cirujanos)) :

            if self.lista_cirujanos[indice_cirujano].disponibilidad == True : 

                return indice_cirujano 
            
            else :
                
                print("No hay cirujanos disponibles para la cirugia")
                return False 


        
##########################################################################################################################################################################





    def asignar_ambulancia (self) -> Union[auto,bool] :


        """ Este metodo busca que una ambulancia este disponible y la envia hacer el viaje """


        for indice_ambulancia in range(len(self.lista_ambulancias)) :


            if self.lista_ambulancias[indice_ambulancia].disponibilidad == True :

                self.lista_ambulancias[indice_ambulancia].disponibilidad = False


                return indice_ambulancia

            else :


                print("No hay ambulancias disponibles para el viaje")
                return False
    



##########################################################################################################################################################################



    def asignar_helicoptero (self) -> Union[helicoptero,bool] :


        """ Este metodo busca que helicoptero este disponible y lo envia a hacer el viaje """


        for indice_helicoptero in range(len(self.lista_helicopteros)):

            if self.lista_helicopteros[indice_helicoptero].disponibilidad == True:

                self.lista_helicopteros[indice_helicoptero].disponibilidad = False


                return indice_helicoptero


            else :

                print("No hay helicopteros disponibles para el viaje")
                return False
    
                

###########################################################################################################################################################################
        
    

    
    def asignar_avion (self) -> Union[avion,bool] :

        """ Este metodo busca que avion este disponible y lo envia a hacer el viaje """


        for indice_avion in range(len(self.lista_aviones)) :

            if self.lista_aviones[indice_avion].disponibilidad == True :


                self.lista_aviones[indice_avion].disponibilidad = False


                return indice_avion

            else :


                print("No hay aviones disponibles para el viaje")
                return False
        

###########################################################################################################################################################################


        
    def direccion_completa(self) -> str :


        """ Este metodo devuelve la direccion completa del centro de salud """

        direccion = f"{self.direccion}, {self.partido}, {self.provincia }" 

        return direccion
