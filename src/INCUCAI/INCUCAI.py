from centrosalud.centro_salud import centro_salud
from Pacientes.donante import donante
from Pacientes.receptor import receptor
from typing import List,Union
from datetime import datetime, date



class INCUCAI () :

    
    def __init__(self, lista_centros_salud : List[centro_salud], lista_donantes : List[donante], lista_receptores : List[receptor]):


        self.lista_centros_salud = lista_centros_salud 
        self.lista_donantes = lista_donantes
        self.lista_receptores = lista_receptores


    # METODOS MAGICOS : 


    def __str__(self) -> str :

        " Presentacion basica del INCUCAI con sus datos  "

        return f"Centros de salud inicial : {self.lista_centros_salud} , lista de donantes : {self.lista_donantes} , lista de receptores {self.lista_receptores}"
    

    def __len__(self) -> int:

    
        "Devuelve la cantidad de elementos totales de centro de salud , lista de donantes y lista_receptores"

        return len(self.lista_centros_salud) + len(self.lista_donantes) + len(self.lista_receptores)



    def __getitem__(self, indice)-> Union[ centro_salud , donante , receptor] : # Ver despues ... mas largo de lo que pense

        """ Este metodo  permite acceder a los elementos de la clase INCUCAI como si fuera una lista.
    Combina centros de salud, donantes y receptores en una sola lista temporal, y devuelve el elemento
    ubicado en la posición indice """

        combinacion_objetos =  self.centros_salud + self.lista_donantes + self.lista_receptores

        return combinacion_objetos[indice]




###########################################################################################################################################################################################################




    def revision_fecha(self, fecha_actual : date) -> date :


        fecha_actual_aux = date.today() # Fecha actual auxiliar para comparar con la fecha actual 
        


        if fecha_actual == fecha_actual_aux :


            return fecha_actual # Si la fecha actual es igual a la fecha auxiliar, no se hace nada y se retorna la fecha actual
        


        elif fecha_actual != fecha_actual_aux :


            self.reiniciar_disponibilidad_y_revisar_donantes() # Si la fecha actual es diferente a la fecha auxiliar, se reinicia la disponibilidad de los vehiculos y se revisan los donantes
            return fecha_actual_aux # retorno la fecha actual auxiliar




############################################################################################################################################################################################################

            
    def reiniciar_disponibilidad_y_revisar_donantes(self) :


        """ Este metodo reinicia la disponibilidad de los vehiculos de los centros de salud y revisa los donantes que han fallecido hace mas de 20 dias  """



        for indice_centro_salud in range(len(self.lista_centros_salud)) :
            self.lista_centros_salud[indice_centro_salud].reiniciar_disponibilidad() # Reinicio la disponibilidad de los vehiculos de cada centro de salud 



        hoy = datetime.today() # Obtengo la fecha actual para comparar con la fecha de fallecimiento de los donantes
        eliminados = 0 # Contador de donantes eliminados
        nuevos_donantes = [] # Lista para almacenar los donantes que no han sido eliminados



        for indice_donante in range(len(self.lista_donantes)) :



            if self.lista_donantes[indice_donante].fecha_hora_fallecimiento is None :

                nuevos_donantes.append(self.lista_donantes[indice_donante]) # Agrego a la lista  los nuevos donantes que no hayan fallecidos 



            else :  # este else se ejecuta si el donante tiene una fecha de fallecimiento registrada

                diferencia = hoy - self.lista_donantes[indice_donante].fecha_hora_fallecimiento # Calculo la diferencia entre la fecha actual(datetime.today()) y la fecha de fallecimiento del donante


                if diferencia.days <= 20: # si la diferencia es menor o igual a 20 dias, el donante no ha fallecido hace mas de 20 dias
                    
                    nuevos_donantes.append(self.lista_donantes[indice_donante]) # Agrego a la lista los donantes que no han fallecido hace mas de 20 dias

                else: # si la diferencia es mayor a 20 dias, el donante ha fallecido hace mas de 20 dias , es decir no puede donar mas organos 

                    print(f"El donante {self.lista_donantes[indice_donante].nombre} ha fallecido hace más de 20 días, se eliminará de la lista")
                    eliminados += 1

        self.lista_donantes = nuevos_donantes # actualizo la lista de donantes con los nuevos donantes que no han fallecido hace mas de 20 dias

        if eliminados == 0 :

            print("No se eliminó ningún donante")
            return None
        
        else :

            print(f"Se eliminaron {eliminados} donantes de la lista")

        return None
    



############################################################################################################################################################################################################






    def menu_centros_salud(self) -> None:

        """ Este metodo imprime un menu con las opciones de centros de salud """

        while True:

            print("1. Imprimir centros de salud")
            print("2. Agregar centro de salud")
            print("3. Seleccionar centro de salud")
            print("4. Eliminar centro de salud")
            print("5. Salir")
            print("\n")

            opcion = input("Seleccione una opción: ")
            print ("\n")

            if opcion == "1":
                self.imprimir_centros_salud()
            if opcion == "2":
                self.ingresar_centro_salud()
            if opcion == "3":
                self.seleccionar_centro_salud()
            if opcion == "4":
                self.eliminar_centro_salud()
            if opcion == "5":
                print("Saliendo del menu de centros de salud")
                return None
            else:
                print("Opcion no valida")


############################################################################################################################################################################################################




    def imprimir_centros_salud(self) -> None:
        """ Imprimo la lista de centros de salud """
        for centro in self.lista_centros_salud:
            print(centro)
            print ("----------------------------------")
        return None



#############################################################################################################################################################################################################



    def ingresar_centro_salud(self) -> None :


        """Este metodo permite ingresar los datos de un centro de salud"""


        print("Ingrese los datos del centro de salud:")


        nombre = input("\nIngrese el nombre del centro de salud:")
        

        indice_centro = self.buscar_centro_salud_por_nombre(nombre)


        if indice_centro is not None:

            print("El centro de salud ya existe")
            return None # retorna none ya que se encontro un nombre de centro de salud repetido 


        # En caso de que no se encuentre en la lista se agregan los datos de este nuevo 

        direccion = input("\nIngrese la direccion del centro de salud:")
        partido = input("\nIngrese el partido del centro de salud:")
        provincia = input("\nIngrese la provincia del centro de salud:")
        telefono_str = input("\nIngrese el telefono del centro de salud:")


        try : # intento convertir el telefono a un entero, si no se puede, se captura la excepcion y se imprime un mensaje de error


            telefono = int(telefono_str)


        except ValueError : # si el telefono no es un numero entero, se captura la excepcion y se imprime un mensaje de error

            print("El telefono debe ser un numero entero")

            return None
        
        
        centro_nuevo = centro_salud(nombre, direccion, partido, provincia, telefono,[],[],[],[]) # Me creo el nuevo centro de salud con los datos ingresados recientemente 



        if len(self.lista_centros_salud) == 0 : # si hay solo un centro de salud en la lista, se agrega directamente el nuevo centro de salud sin verificar si el telefono ya existe



            self.lista_centros_salud.append(centro_nuevo)
            print("Centro guardado correctamente")
            return None


        # si hay mas de un centro de salud en la lista, se verifica si el telefono ya existe en la lista de centros de salud

        for indice_centro_salud in range(len(self.lista_centros_salud)):

            if self.lista_centros_salud[indice_centro_salud].telefono == centro_nuevo.telefono:
                print("El telefono del centro de salud ya existe")
                return None
            

        self.lista_centros_salud.append(centro_nuevo)
        print("Centro guardado correctamente")
        return None

    



##############################################################################################################################################################################################################



    def seleccionar_centro_salud(self) -> None :


        """Este metodo permite seleccionar un centro de salud de la lista"""


        nombre_centro = input("Ingrese el nombre del centro de salud que desea seleccionar:")

        indice_centro = self.buscar_centro_salud_por_nombre(nombre_centro)


        if indice_centro is None : # si no se devuelve el indice , significa que el centro de salud no se encuenta , entonces ...
            
            print("El centro de salud no existe")
            return None


        else :

            print("Centro encontrado")
            self.lista_centros_salud[indice_centro].menu_institucion()
            return None
    


    ##########################################################################################################################################################################################################



    def eliminar_centro_salud(self):


        """Este metodo sirve para eliminar un centro de salud con .pop ccon sus rspectivos donantes y receptores """

        
        nombre_centro = input("Ingrese el centro que desea eliminar:")


        indice_centro = self.buscar_centro_salud_por_nombre(nombre_centro)



        if indice_centro is None:

            print("El centro de salud no existe")


        else :


            self.lista_centros_salud.pop(indice_centro)
            
            print("Centro eliminado correctamente")
            




            print("A continuacion se eliminara los donantes y receptores asociados al centro de salud")




            for indice_donante in range (len(self.lista_donantes)):
                
                if self.lista_donantes[indice_donante].centro_salud == nombre_centro :
                    
                    self.lista_donantes.pop(indice_donante)


                else :

                    print("No se encontraron donantes asociados al centro de salud")





            for indice_receptor in range (len(self.lista_receptores)):

                if self.lista_receptores[indice_receptor].centro_salud == nombre_centro :
                    
                    self.lista_receptores.pop(indice_receptor)

                else :

                    print("No se encontraron receptores asociados al centro de salud")





            print("operacion finalizada correctamente")


    


##############################################################################################################################################################################################################
            

    def menu_donantes(self):
        """ Este metodo imprime un menu con las opciones de los donantes """
        while True:
            print("1.Imprimir donantes")
            print("2.Agregar donante")
            print("3.Editar donante")
            print("4.Eliminar donante")
            print("5.Salir")
            print("\n")

            opcion = input("Seleccione una opción: ")
            print ("\n")

            if opcion == "1":
                self.imprimir_donantes()
            if opcion == "2":
                self.agregar_donante()
            if opcion == "3":
                self.editar_donante()
            if opcion == "4":
                self.eliminar_donante()
            if opcion == "5":
                print("Saliendo del menu de donantes")
                return None


##############################################################################################################################################################################################################



    def imprimir_donantes(self) -> None:
        """ Imprimo la lista de donantes"""
        for donante in self.lista_donantes:
            print(donante)
            print ("----------------------------------")
        return None


###############################################################################################################################################################################################################




    
    def agregar_donante(self)->None :

        """ Este metodo permite ingresar los datos de un donante """


        organos = ["Corazon", "Pulmon izquierdo", "Pulmon derecho", "Riñon izquierdo", "Riñon derecho", "Higado", "Pancreas", "Intestino", "Piel", "Corneas", "Hueso"] # lista de organos disponibles para donar

        print("Ingrese los datos del donante:")

        nombre = input("Ingrese el nombre del donante:")
        dni_str = input("Ingrese el DNI del donante:")


        try : # intento convertir el dni a un entero, si no se puede, se captura la excepcion y se imprime un mensaje de error

            dni = int(dni_str)  # Convertir a entero


        except ValueError :

            print("DNI no válido") # mensaje de error que aparece cuando falla el bloque try
            return None


        indice_receptor = self.buscar_receptor_por_dni(dni) # busco si el dni del receptor coincide con alguno de los receptores registrados en la lista de receptores


        if indice_receptor is not None : # si el dni coincide con uno de la lista
            print("DNI ya registrado")
            return None
        



        indice_donante = self.buscar_donante_por_dni(dni) # busco si el dni del donante coincide con alguno de los donantes registrados en la lista de donantes


        if indice_donante is not None: # si el dni coincide con uno de la lista
            print("DNI ya registrado")
            return None


            
        fecha_nacimiento_str = input("Ingrese la fecha de nacimiento del donante (DD/MM/AAAA):")


        try : # intento convertir la fecha de nacimiento a un objeto datetime, si no se puede, se captura la excepcion y se imprime un mensaje de error
        

            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")  # Convertir a objeto datetime
            
            
        except ValueError : # este bloque se ejecuta cuando el bloque try falla , es decir cuando la fecha de nacimiento no es valida


            print("Fecha de nacimiento no válida")
            return None 



        hoy = datetime.today() # Obtengo la fecha actual para calcular la edad del donante
        
        edad = hoy.year - fecha_nacimiento.year # Calculo la edad del donante restando el año de nacimiento al año actual


        if (hoy.month , hoy.day) < (fecha_nacimiento.month,fecha_nacimiento.day): # Por si no cumplio años
            edad -= 1


        elif edad < 18: #Verifico que el donante sea mayor de edad
        
            print("El paciente es menor de edad, no se puede ingresar")
            return None
        

        
        sexo = input("Ingrese el sexo del donante (M/F):") # pido el genero 

        if sexo not in ['M', 'F'] : # si el sexo no es M o F, se imprime un mensaje de error y se retorna None
            
            print("Sexo no válido, debe ser M o F")
            return None

        


        telefono_str = input("Ingrese el telefono del donante:") # pido el telefono del donante 
        
        try : # intento convertir el telefono a un entero, si no se puede, se captura la excepcion y se imprime un mensaje de error

            telefono = int(telefono_str)  # Convertir a entero

        except ValueError : # este bloque se ejecuta cuando el bloque try falla , es decir cuando el telefono no es valido
        
            print("Telefono no válido")
            return None
        
        
            
            
        tipo_sangre = input("Ingrese el tipo de sangre del donante (A+, A-, B+, B-, AB+, AB-, O+, O-):") # pido el tipo de sangre del donante



        if tipo_sangre not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'] : # # si el tipo de sangre no es uno de los tipos validos, se imprime un mensaje de error y se retorna None

            print("Tipo de sangre no válido")
            return None



        fecha_fallecimiento_str = input("Ingrese la fecha de fallecimiento del donante (DD/MM/AAAA), si no esta muerto ingrese 'No':") # pido la fecha de fallecimiento del donante

        if fecha_fallecimiento_str.lower() == 'no': # si el donante no ha fallecido, se asigna None a la fecha de fallecimiento , osea no fallecio

            fecha_fallecimiento = None


        else : 
            
            try : # intento convertir la fecha de fallecimiento a un objeto datetime, si no se puede, se captura la excepcion y se imprime un mensaje de error
                
                
                fecha_fallecimiento = datetime.strptime(fecha_fallecimiento_str, "%d/%m/%Y")  # Convertir a objeto datetime


            except ValueError : # se ejecuta cuando el bloque try falla , es decir cuando la fecha de fallecimiento no es valida 

                print("Fecha de fallecimiento no válida")
                return None
            


        centro_salud = input("Ingrese el centro de salud del donante:") # pido el centro de salud del donante 


        for indice_centro_salud in range(len(self.lista_centros_salud)) :
            
            
            if self.lista_centros_salud[indice_centro_salud].nombre == centro_salud :
                break
                
            # si el centro de salud se encuentra en la lista de centros de salud, se sale del bucle , observo ese indice y lo uso para asignar el centro de salud al donante

            if indice_centro_salud == len(self.lista_centros_salud) - 1: # # si se llega al final de la lista y no se encuentra el centro de salud, se imprime un mensaje de error y se retorna None
                
                print("El centro de salud no existe")
                return None


        print("A continuacion se mostraran los organos disponibles, ingrese el numero correspondiente, para dejar de ingresar coloque un 0") 
        
        
        for indice_organo in range(len(organos)) : # muestro los organos disponibles para donar


            print(f"{indice_organo+1}. {organos[indice_organo]}\n") # imprimo los organos disponibles con su respectivo numero


        lista_organos = [] # lista para almacenar los organos que el donante desea donar
        
        while True : # bucle para ingresar los organos que el donante desea donar
            
            
            
            indice = int(input("Ingrese el organo que desea donar:"))

            if indice > 0 and indice <=len(organos) : # si el indice es valido, se agrega el organo a la lista de organos del donante , osea esta dentro de la lista 
                

                lista_organos.append(organos[indice-1]) # agrego el organo a la lista de organos del donante, restando 1 al indice para que coincida con el indice de la lista de organos

            if (indice<1 or indice>len(organos)) and len(lista_organos) == 0 : # si el indice no es valido y la lista de organos esta vacia, se imprime un mensaje de error y se vuelve a pedir el organo
            
                print("Debe ingresar al menos un organo")
                
            if (indice<1 or indice>len(organos)) and len(lista_organos)>=1 : # si el indice no es valido y la lista de organos tiene al menos un organo, se imprime un mensaje de confirmacion y se sale del bucle
                
                print("Organos ingresados correctamente")
                break
            


        nuevo_donante = donante(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, fecha_fallecimiento, lista_organos, []) # Me creo el nuevo donante con los datos ingresados recientemente

        self.lista_donantes.append(nuevo_donante) # agrego el nuevo donante a la lista de donantes


        indice_receptor = self.match_donante() # busco un receptor que coincida con el donante que acabo de agregar
        indice_donante = len(self.lista_donantes)-1

        if indice_receptor == False:
            print ("Se realizo la busqueda y no se encontro a ningun receptor")
        elif isinstance(indice_receptor, int):
            decision_cirugia = input("Se encontro a receptor disponible, desea continuar con la cirugia? (Si/No):")
            if decision_cirugia.lower() == "si":
                indice_centro_donante = self.buscar_centro_salud_por_nombre(self.lista_donantes[indice_donante].centro_salud)
                indice_centro_receptor = self.buscar_centro_salud_por_nombre(self.lista_receptores[indice_receptor].centro_salud)
                for indice_organo in range(len(self.lista_donantes[indice_donante].lista_organos)):
                    if self.lista_donantes[indice_donante].lista_organos[indice_organo] == self.lista_receptores[indice_receptor].organo:
                        break
                self.proceso_cirugia(indice_donante, indice_receptor, indice_centro_donante, indice_centro_receptor, indice_organo)
            else:
                return None
        return None


#############################################################################################################################################################################################################


    def editar_donante(self) -> None :
        """ Este metodo permite editar los datos de un donante """

        organos = ["Corazon", "Pulmon izquierdo", "Pulmon derecho", "Riñon izquierdo", "Riñon derecho", "Higado", "Pancreas", "Intestino", "Piel", "Corneas", "Hueso"]
        dni_str = input("Ingrese el DNI del donante que desea editar:")


        try: # Intento convertir el dni a un tipo de dato str dentro del bloque try

            dni = int(dni_str)

        except ValueError: # se ejecuta cuando el bloque try falla , lanzando una advertencia de DNI no valido
        
            print("DNI no válido")
            return None


        indice_donante = self.buscar_donante_por_dni(dni) # busco al dona
        if indice_donante is None:
            print("Donante no encontrado")
            return None
        else:
            print("Donante encontrado")
            print("Ingrese los nuevos datos del donante:")
            fecha_fallecimiento_str = input("Ingrese la fecha de fallecimiento del donante (DD/MM/AAAA):")
            try:
                fecha_fallecimiento = datetime.strptime(fecha_fallecimiento_str, "%d/%m/%Y")  # Convertir a objeto datetime
            except ValueError:
                print("Fecha de fallecimiento no válida")
                return None
            print("A continuacion se mostraran los organos disponibles, ingrese el numero correspondiente, para dejar de ingresar coloque un 0")
            for i in range(len(organos)):
                print(f"{i+1}. {organos[i]}\n")
            lista_organos = []
            while True:
                x = int(input("Ingrese el organo que desea donar:"))
                if x>0 and x<=len(organos):
                    lista_organos.append(organos[x-1]) # agrego el organo a la lista de organos del donante
                if (x<1 or x>len(organos)) and len(lista_organos) == 0:
                    print("Debe ingresar al menos un organo")
                if (x<1 or x>len(organos)) and len(lista_organos)>=1:
                    print("Organos ingresados correctamente")
                    break
            self.lista_donantes[indice_donante].fecha_hora_fallecimiento = fecha_fallecimiento
            self.lista_donantes[indice_donante].lista_organos = lista_organos
            indice_receptor= self.match_donante()

            if indice_receptor == False:
                print ("Se realizo la busqueda y no se encontro a ningun receptor")
            elif isinstance(indice_receptor, int):
                decision_cirugia = input("Se encontro a un receptor disponible, desea continuar con la cirugia? (Si/No):")
                if decision_cirugia.lower() == "si":
                    indice_centro_donante = self.buscar_centro_salud_por_nombre(self.lista_donantes[indice_donante].centro_salud)
                    indice_centro_receptor = self.buscar_centro_salud_por_nombres(self.lista_receptores[indice_receptor].centro_salud)
                    for indice_organo in range(len(self.lista_donantes[indice_donante].lista_organos)):
                        if self.lista_donantes[indice_donante].lista_organos[indice_organo] == self.lista_receptores[indice_receptor].organo:
                            break
                    self.proceso_cirugia(indice_donante, indice_receptor, indice_centro_donante, indice_centro_receptor, indice_organo)
            else:
                return None
            return None


    def eliminar_donante(self):
        """Este metodo permite eliminar a un donante de la lista con .pop()"""
        dni_str = input("Ingrese el DNI del donante que desea eliminar:")
        try:
            dni = int(dni_str)  # Convertir a entero
        except ValueError:
            print("DNI no válido")
            return None
        indice_donante = self.buscar_donante_por_dni(dni)
        if indice_donante is None:
            print("Donante no encontrado")
            return None
        else:
            self.lista_donantes.pop(indice_donante)
            print("Donante eliminado correctamente")
            return None
#############################################################################################################################################################################################################


    def menu_receptores(self):
        """ Este metodo imprime un menu con las opciones de los receptores """
        while True:
            print("Bienvenido al menu de receptores:")
            print("1.Imprimir receptores")
            print("2.Agregar receptor")
            print("3.Editar receptor")
            print("4.Eliminar receptor")
            print("5.Salir")
            print("\n")

            opcion = input("Seleccione una opcion:")

            if opcion == "1":
                self.imprimir_receptores()
            if opcion == "2":
                self.agregar_receptor()
            if opcion == "3":
                self.editar_receptor()
            if opcion == "4":
                self.eliminar_receptor()
            if opcion == "5":
                print("Saliendo del menu de receptores")
                return None


#############################################################################################################################################################################################################



    def imprimir_receptores(self) -> None:
        """ Imprimo la lista de receptores"""
        for receptor in self.lista_receptores:
            print(receptor)
            print ("----------------------------------")
        return None


###########################################################################################################################################################################################################



    def agregar_receptor(self)-> None :

        """ Este metodo permite ingresar los datos de un receptor """

        
        organos = ["Corazon", "Pulmon izquierdo", "Pulmon derecho", "Riñon izquierdo", "Riñon derecho", "Higado", "Pancreas", "Intestino", "Piel", "Corneas", "Hueso"] # lista g
        print("Ingrese los datos del receptor:")

        nombre = input("Ingrese el nombre del receptor:")
        dni_str = input("Ingrese el DNI del receptor:")

        try: #Reviso que el dni se pueda convertir a int, en caso de que no se pueda tira error  retorna la funcion
            dni = int(dni_str)  

        except ValueError: 

            print("DNI no válido")
            return None
        
        indice_receptor = self.buscar_receptor_por_dni(dni) #Luego reviso ambas listas y controlo que no se repita el dni
        if indice_receptor is not None:
            print("DNI ya registrado")
            return None
        indice_donante = self.buscar_donante_por_dni(dni)
        if indice_donante is not None:
            print("DNI ya registrado")
            return None
        fecha_nacimiento_str = input("Ingrese la fecha de nacimiento del donante (DD/MM/AAAA):") #Pido que ingresen la fecha de nacimiento y controlo que la hayan escrito correctamente
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")  # Convertir a objeto datetime
        except ValueError:
            print("Fecha de nacimiento no válida")
            return None
        sexo = input("Ingrese el sexo del donante (M/F):") #Se ingresa el genero
        if sexo not in ['M', 'F']:
            print("Sexo no válido, debe ser M o F")
            return None
        telefono_str = input("Ingrese el telefono del donante:") #Ingreso el numero de telefono del paciente y vuelvo a controlar que sea un int
        try:
            telefono = int(telefono_str)  # Convertir a entero
        except ValueError:
            print("Telefono no válido")
            return None
        tipo_sangre = input("Ingrese el tipo de sangre del donante (A+, A-, B+, B-, AB+, AB-, O+, O-):") #Pido que ingresen el tipo de sangre y reviso que se haya ingresado correctamente
        if tipo_sangre not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']:
            print("Tipo de sangre no válido")
            return None
        centro_salud = input("Ingrese el centro de salud del donante:") #Ingreso el centro de salud y compruebo que exista este
        for indice_centro_salud_receptor in range(len(self.lista_centros_salud)):
            if self.lista_centros_salud[indice_centro_salud_receptor].nombre == centro_salud:
                break
            if x == len(self.lista_centros_salud) - 1:
                print("El centro de salud no existe")
                return None
        print("A continuacion se mostraran los organos disponibles, ingrese el numero correspondiente al organo que necesita") #Les pongo una lista de opciones para que seleccionen el organo necesits el receptor
        for i in range(len(organos)):
            print(f"{i+1}. {organos[i]}\n")
        x = int(input("Ingrese el organo que necesita:"))
        if x<1 or x>len(organos):
            print("Organo no valido")
            return None
        organo = organos[x-1]  # asigno el organo a la variable organo
        fecha_inscripcion = datetime.now()#La fecha de inscripcion se ingresa de forma automatica
        prioridad_str = input("Ingrese la prioridad del receptor (1-10):")
        try:
            prioridad = int(prioridad_str)#ingresan su prioridad, del 1 al 10
        except ValueError:
            print("Prioridad no válida, debe ser un número entero")
            return None
        if prioridad < 1 or prioridad > 10:
            print("Prioridad no válida, debe ser un número entre 1 y 10")
            return None
        patologia = input("Ingrese la patologia del receptor:") #ingresa la patologia del receptor
        estable_str = input("Ingrese si el receptor esta estable (Si/No):")#Ingreso la estabilidad
        if estable_str.lower() == 'si':
            estable = True
        elif estable_str.lower() == 'no':
            estable = False
        else:
            print("Estado no válido, debe ser Si o No")
            return None
        #Creo y guardo al receptor
        nuevo_receptor = receptor(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, organo, fecha_inscripcion, prioridad, patologia, estable) 
        self.lista_receptores.append(nuevo_receptor)
        print("Receptor agregado correctamente")

        indice_donante = self.match_receptor() #Mismo proceso que en editar_receptor
        indice_receptor = len(self.lista_receptores)-1

        if indice_donante == False:
            print ("Se realizo la busqueda y no se encontro a ningun donante")
        elif isinstance(indice_donante, int):
            decision_cirugia = input("Se encontro a un donante disponible, desea continuar con la cirugia? (Si/No):")
            if decision_cirugia.lower() == "si":
                indice_centro_donante = self.buscar_centro_salud_por_nombre(self.lista_donantes[indice_donante].centro_salud)
                for indice_organo in range(len(self.lista_donantes[indice_donante].lista_organos)):
                    if self.lista_donantes[indice_donante].lista_organos[indice_organo] == self.lista_receptores[indice_receptor].organo:
                        break
                self.proceso_cirugia(indice_donante, indice_receptor, indice_centro_donante, indice_centro_salud_receptor, indice_organo)
            else:
                return None


############################################################################################################################################################################################################



    def editar_receptor(self):


        """ Este metodo permite editar la prioridad y la estabilidad del receptor"""

        dni_str = input("Ingrese el DNI del receptor que desea editar:")


        try: # Controlo poder convertir el dni a un int para corroborar que l
            
            dni = int(dni_str)  # Convertir a entero

        except ValueError: # este bloque se ejecuta cuando hay una falla en el try
             
            print("DNI no válido")
            return None
        
        
        indice_receptor = self.buscar_receptor_por_dni(dni) # busco al receptor por su dni 



        if indice_receptor is None : # si el indice es none ose que no se encontro el DNI .....
            
            print("Receptor no encontrado")
            return None
        
        else : # En caso que se halla encontrado el dni del receptor ... (Comienzo a ingresar los datos)
            
            print("Receptor encontrado")
            print("Ingrese los nuevos datos del receptor:")

            prioridad_str = input("Ingrese la prioridad del receptor (1-10):")

            try : # se ejecuta el bloque try en el primer instante 

                prioridad = int(prioridad_str)

            except ValueError: # esta excepcion se ejecuta cuando se produce un error en el bloque try  
                
                print("Prioridad no válida, debe ser un número entero")
                return None
            

            if prioridad < 1 or prioridad > 10: 

                print("Prioridad no válida, debe ser un número entre 1 y 10")
                return None

            estable_str = input("Ingrese si el receptor esta estable (Si/No):")

            if estable_str.lower() == 'si': # convierto la respuesta del usuario en minuscula en caso de que sea mayuscula 
                
                estable = True # cambio su estabilidad a verdadero


            elif estable_str.lower() == 'no': # convierto la respuesta del usuario en minuscula en caso de que sea mayuscula
                 
                estable = False # cambio la estabilidad a falso


            self.lista_receptores[indice_receptor].prioridad = prioridad # actualizo la prioridad del receptor indice receptor de la lista 
            self.lista_receptores[indice_receptor].estable = estable # actualizo la estabilidad del receptor indice receptor de la lista
            print("Receptor editado correctamente")

            indice_donante = self.match_receptor() # Llamo al match

            if indice_donante == False : #Si el match retorna falso es porque no encontro ningun donante
                print ("Se realizo la busqueda y no se encontro a ningun donante")



            elif isinstance(indice_donante, int): # Si si devolvio un indice, damos la opcion al usuario de seguir con la cirugia
                
                decision_cirugia = input("Se encontro a un donante disponible, desea continuar con la cirugia? (Si/No):")

                if decision_cirugia.lower() == "si": #En caso de que diga que si buscamos los indices de los centros tanto del donante como del receptor y del organo que donara el donante, luego llamamos al proceso de cirugia
                    indice_centro_donante = self.buscar_centro_salud_por_nombre(self.lista_donantes[indice_donante].centro_salud)
                    indice_centro_receptor = self.buscar_centro_salud_por_nombre(self.lista_receptores[indice_receptor].centro_salud)
                    for indice_organo in range(len(self.lista_donantes[indice_donante].lista_organos)):
                        if self.lista_donantes[indice_donante].lista_organos[indice_organo] == self.lista_receptores[indice_receptor].organo:
                            break
                    self.proceso_cirugia(indice_donante, indice_receptor, indice_centro_donante, indice_centro_receptor, indice_organo) #aca llamamos al proceso de cirugia
                else:
                    return None
            return None
    

##############################################################################################################################################################################################################



    def eliminar_receptor(self)-> None :

        """Este metodo permite eliminar a un receptor de la lista con .pop()"""

        dni_str = input("Ingrese el DNI del receptor que desea eliminar:")

        try : # intento convertir el dni a un entero, si no se puede, se captura la excepcion y se imprime un mensaje de error

            dni = int(dni_str)  # Convertir a entero

        except ValueError : # este bloque se ejecuta cuando el bloque try falla , es decir cuando el dni no es valido

            print("DNI no válido")

            return None


        indice_receptor = self.buscar_receptor_por_dni(dni) # busco si el dni del receptor coincide con alguno de los receptores registrados en la lista de receptores

        if indice_receptor is None : # si no se devuelve el indice , significa que el receptor no se encuenta , entonces ...

            print("Receptor no encontrado")
            return None
        
        else : # si se devuelve el indice , significa que el receptor se encuenta en la lista de receptores

            self.lista_receptores.pop(indice_receptor)
            print("Receptor eliminado correctamente")
            return None



##############################################################################################################################################################################################################



    def buscar_donante_por_dni(self, dni : int)-> Union[int,None] :

        for indice_donante in range (len(self.lista_donantes)) :

            if self.lista_donantes[indice_donante].dni == dni :
                return indice_donante
            
        return None



##############################################################################################################################################################################################################



    def buscar_receptor_por_dni(self ,dni : int) -> Union[int,None] :

        for indice_receptores in range(len(self.lista_receptores)):

            if self.lista_receptores[indice_receptores].dni == dni:
                return indice_receptores
            
        return None



#############################################################################################################################################################################################################


    def buscar_centro_salud_por_nombre(self, nombre: str) -> Union[int,None] :

        
        """Este metodo busca un centro de salud por su nombre y devuelve su indice en la lista de centros de salud o None si no lo encuentra """


        for indice_centro_salud in range(len(self.lista_centros_salud)) :


            if self.lista_centros_salud[indice_centro_salud].nombre == nombre:

                return indice_centro_salud


        return None # se retorna none cuando 


##############################################################################################################################################################################################################



    def proceso_cirugia(self, indice_donante: int, indice_receptor : int, indice_centro_salud_donante : int, indice_centro_salud_receptor: int, indice_organo_donante : int) -> None :
        """Este metodo se encarga de realizar el proceso de cirugia del donante, asignando un cirujano y realizando la ablacion del organo"""
        
        cirugia = self.cirujia_donante(indice_donante, indice_centro_salud_donante, indice_centro_salud_receptor, indice_organo_donante) #Llamo a cirugia para el donante

        if cirugia == -1:
            print("No se pudo hacer la cirugia ya que no hay suficientes cirujanos disponibles") #Si no hay suficientes cirujanos se cancela
            return None
        if cirugia == -2:
            print("La ablacion no fue exitosa, por lo que no habra transplante") #Si la ablacion fracasa se cancela
            return None
        if cirugia == 1:
            print("La ablacion fue un exito") #en este caso se sigue la cirujia
        

        direccion_centro_donante = self.lista_centros_salud[indice_centro_salud_donante].direccion_completa()
        direccion_centro_receptor = self.lista_centros_salud[indice_centro_salud_receptor].direccion_completa()
        

        """Reviso cada caso particular segun la ubicacion del centro, mismo centro, distinta provincia, distinta ciudad o distinta direccion, luego asigno un vehiculo y realizo el viaje"""



        if self.lista_donantes[indice_donante].centro_salud == self.lista_receptores[indice_receptor].centro_salud: 
            print("El donante y el receptor pertenecen al mismo centro de salud, por lo que no se debe hacer ningun viaje")


        if self.lista_centros_salud[indice_centro_salud_donante].provincia != self.lista_centros_salud[indice_centro_salud_receptor].provincia:
            
            indice_vehiculo = self.lista_centros_salud[indice_centro_salud_donante].asignar_avion()
            viaje = self.lista_centros_salud[indice_centro_salud_donante].lista_aviones[indice_vehiculo].calcular_tiempo_viaje(direccion_centro_donante,direccion_centro_receptor)
            print(f"El envio del organo durara {viaje} horas")
            
            
        if self.lista_centros_salud[indice_centro_salud_donante].provincia == self.lista_centros_salud[indice_centro_salud_receptor].provincia and self.lista_centros_salud[indice_centro_salud_donante].partido != self.lista_centros_salud[indice_centro_salud_receptor].partido:
            
            indice_vehiculo = self.lista_centros_salud[indice_centro_salud_donante].asignar_helicoptero()
            viaje = self.lista_centros_salud[indice_centro_salud_donante].lista_helicopteros[indice_vehiculo].calcular_tiempo_viaje(direccion_centro_donante,direccion_centro_receptor)
            print (f"El envio del organo durara {viaje} horas")
            
        if self.lista_centros_salud[indice_centro_salud_donante].provincia == self.lista_centros_salud[indice_centro_salud_receptor].provincia and self.lista_centros_salud[indice_centro_salud_donante].partido == self.lista_centros_salud[indice_centro_salud_receptor].partido and self.lista_centros_salud[indice_centro_salud_donante].direccion != self.lista_centros_salud[indice_centro_salud_receptor].direccion:
            
            indice_vehiculo = self.lista_centros_salud[indice_centro_salud_donante].asignar_ambulancia()
            viaje = self.lista_centros_salud[indice_centro_salud_donante].lista_ambulancias[indice_vehiculo].calcular_tiempo_viaje(direccion_centro_donante,direccion_centro_receptor)
            print(f"El envio del organo durara {viaje} horas")

        
        if len(self.lista_donantes[indice_donante].lista_organos) == 0:# Si el donante queda con 0 organos se elimina
            self.lista_donantes.pop(indice_donante)
            print("Se ha eliminado al donante de la lista ya que no tiene mas organos para donar")



        cirugia_receptor = self.cirujia_receptor(indice_receptor, indice_centro_salud_receptor) # Realizo la cirujia del receptor

        if cirugia_receptor == 1: #Caso en el que fue un exito, con .pop(indice) borro un elemento de la lista teniendo en cuenta su posicion
            print("El transplante ha sido un exito")
            self.lista_receptores.pop(indice_receptor)
            return None
        elif cirugia_receptor == -1: #Caso en el que fue un fracaso, cambio su prioridad a 10 y su estabilidad a falsa
            print("El transplante ha salido mal, asignando maxima prioridad al paciente")
            self.lista_receptores[indice_receptor].cambiar_prioridad()
            self.lista_receptores[indice_receptor].cambiar_estable()
            return None



#########################################################################################################################################################################################################
    def match_donante (self)->Union[bool,int]: 

        """Este metodo busca un receptor compatible par un donante teniendo en cuenta el tipo de sangre y el organo """

        lista_aux_1 = [] # me creo una lista auxiliar para almacenar receptores compatibles

        receptor_aux = None # inicializo una variable para el receptor con mayor prioridad 

        indice_donante = len(self.lista_donantes)-1

        for indice_receptor_1 in range(len(self.lista_receptores)) : # recorro la lista de receptores de la lista con indice rec

            if self.lista_donantes[indice_donante].tipo_sangre == self.lista_receptores[indice_receptor_1].tipo_sangre: # se compara el tipo de sangre del donante con el del receptor 
 
                for indice_organo in range(len(self.lista_donantes[indice_donante].lista_organos)): # recorro la lista de organos del donante pasado como parametro del metodo 

                    if self.lista_donantes[indice_donante].lista_organos[indice_organo] == self.lista_receptores[indice_receptor_1].organo : #  verifico si el receptor necesita el órgano que el donante tiene

                        lista_aux_1.append(self.lista_receptores[indice_receptor_1]) # se agrega el receptor compatible a la lista auxiliar 1


        if len(lista_aux_1)==0 : # si la lista esta vacia , esto significa que no hay receptores compatibles 
            return False 
        
        
        elif len(lista_aux_1) == 1: # si solo hay un receptor compatible 
            indice_receptor_lista = self.buscar_receptor_por_dni(lista_aux_1[0].dni)
            return indice_receptor_lista 
        
        

        else :
            
            receptor_aux = lista_aux_1[0] # inicializo  el receptor con el primer elemento de la lista.
            
            for indice_receptor_2 in range(len(lista_aux_1)) : # recorro los receptores en la lista auxiliar

                if receptor_aux.prioridad < lista_aux_1[indice_receptor_2].prioridad :
                    if receptor_aux.estabilidad == False:
                        receptor_aux == lista_aux_1[indice_receptor_2]# comparo la prioridad de los receptores 

                    receptor_aux = lista_aux_1[indice_receptor_2] # actualizo  el receptor con mayor prioridad

            indice_receptor_lista = self.buscar_receptor_por_dni(receptor_aux.dni)

            return indice_receptor_lista # una vez que lo actualizo lo retorno 


#############################################################################################################################################################################################################


    def match_receptor (self)->Union[int,bool] : 
        

        """Este metodo lo que hace es  busacar un donante compatible para un receptor teniendo en cuenta el tipo de sangre y el organo """

        indice_receptor = len(self.lista_receptores)-1

        for indice_donante in range(len(self.lista_donantes)): #Recorro la lista de donantes 
            if self.lista_receptores[indice_receptor].tipo_sangre == self.lista_donantes[indice_donante].tipo_sangre: #comparo que tengan el mismo tipo de sangre
                for indice_organo in range(len(self.lista_donantes[indice_donante].lista_organos)):#recorro la lista de organos del donante si tienen el mismo tipo de sangre
                    if self.lista_donantes[indice_donante].lista_organos[indice_organo] == self.lista_receptores[indice_receptor].organo: #comparo y veo que el donante ofrezca el organo que el receptor necesita
                        return indice_donante  # Donante compatible encontrado, retorno su indice
                    
        return False  # No se encontró donante compatible , retorno falso



#############################################################################################################################################################################################################


    def cirujia_donante(self, donante: int, indice_centro_salud_donante : int , indice_centro_salud_receptor : int, indice_organo_donante : int) -> int : 
        indice_cirujano_donante = self.lista_centros_salud[indice_centro_salud_receptor].asignar_cirujano() 
        indice_cirujano_receptor = self.lista_centros_salud[indice_centro_salud_donante].asignar_cirujano()


        if indice_cirujano_donante == False :
            return -1
        
        elif indice_cirujano_receptor == False : #controlo que existan ambos cirujanos para realizar la cirujia
            return -1

        elif self.lista_centros_salud[indice_centro_salud_donante].lista_cirujanos[indice_cirujano_donante].exito_ablacion(self.lista_donantes[donante], indice_organo_donante) == True: #realizo la cirujia

            self.lista_donantes[donante].actualizar_lista_ablacion(indice_organo_donante)#Añado el proceso de la cirugia a la lista de ablacion
            print("La cirujia fue un exito")
            return 1 #si fue un exito retorno 1

        else:
            self.lista_donantes[donante].actualizar_lista_ablacion(indice_organo_donante)
            return -2 #Si fue un fracaso retorno -2


############################################################################################################################################################################################################


    def cirujia_receptor(self, receptor : int, centro_salud_receptor : int) -> int :

        indice_cirujano_receptor = self.lista_centros_salud[centro_salud_receptor].asignar_cirujano() #asigno cirujano

        if self.lista_centros_salud[centro_salud_receptor].lista_cirujanos[indice_cirujano_receptor].exito_transplante(self.lista_recepto[receptor]) == True: #hago la cirujia
            return 1 #retorno 1 si fue un exito
        else:
            return - 1 #-1 si fue un fracaso

