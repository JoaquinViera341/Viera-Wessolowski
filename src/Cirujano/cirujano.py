import random
from Pacientes.donante import donante
from Pacientes.receptor import receptor

class cirujano () :



    def __init__(self, dni : int, especialidad : str , disponibilidad : bool, nombre : str) :


        self.dni = dni
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad
        self.nombre = nombre
         



#####################################################################################################################################################################

    # METODOS MAGICOS :




    def __str__(self):

        """Este metodo hace una presentacion basica de un cirujano""" 


        if self.disponibilidad == True:

            disponibilidad = "Disponible"

        else:

            disponibilidad = "No Disponible"

        return f"Nombre : {self.nombre} \n Dni : {self.dni} \n Especialidad : {self.especialidad} \n Disponibilidad : {disponibilidad} "
    

    def __eq__(self, other ) :


        " Este metodo lo que hace es comparar dos Cirujanos basandose en sus DNIs . llamo a este metodo desde el main con ej : cirujano_1 == cirujano_2 "

        if isinstance( other , cirujano ) :


            return self.dni == other.dni
        

        return False 





##################################################################################################################################################################
    


    def exito_ablacion(self , donante_obj : donante , organo : int) -> bool :


        """ Este metodo ve si una ablacion  de un organo es exitosa o no  basandose en la especiliazacion y organo """


        
        self.disponibilidad = False



        if donante_obj.lista_organos[organo] == "Corazon" and self.especialidad == "Cardiologo" : 

            random_num = random.randint(1,10) 


            if random_num >= 3 : 
                return True
            

            else : 
                return False
        

        


        elif (donante_obj.lista_organos[organo] == "Riñon izquierdo" or donante_obj.lista_organos[organo] == "Riñon derecho" or donante_obj.lista_organos[organo] == "Higado" or donante_obj.lista_organos[organo] == "Intestinos" or donante_obj.lista_organos[organo] == "Pancreas") and self.especialidad == "Gastroenterologo":



            random_num = random.randint(1,10) 


            if random_num >= 3 : 
                return True 
            
            else :      
                return False
            

         
   
        elif (donante_obj.lista_organos[organo] == "Pulmon izquierdo" or donante_obj.lista_organos[organo] == "Pulmon derecho") and self.especialidad == "Pulmonar":


            random_num = random.randint(1,10) 


            if random_num >= 3 :
                return True 
            
            else : 
                return False
            

        

        elif (donante_obj.lista_organos[organo] == "Piel" or donante_obj.lista_organos[organo] == "Corneas") and self.especialidad == "Plastico" :


            random_num = random.randint(1,10) 


            if random_num >= 3 : 
                return True 
            
            else:
                return False
        

        

        elif donante_obj.lista_organos[organo] == "Hueso" and self.especialidad == "Traumatologo" :

            random_num = random.randint(1,10)


            if random_num >= 3 : 
                return True 
            

            else :
                return False



        # UN CASO DIFERENTE :


        # cuando no se cumplen ninguno de los anteriores casos , determino la probabilidad de la cirujia con menor probabilidad de exito 


        else :

            random_num = random.randint(1,10) 

            if random_num > 5 :
                return True
            

            else:
                return False



####################################################################################################################################################################





    def exito_transplante(self, receptor_obj : receptor) -> bool :



        """Este metodo lo que hace es ver la probabilidad de exito de un transplante basandose en el organo que recibe el paciente y la especialidad del cirujano """

    
        self.disponibilidad = False


        if(receptor_obj.organo == "Corazon") and self.especialidad == "Cardiologo" :


            random_num = random.randint(1,10) 


            if random_num >= 3 :                 
                return True 
            

            else:
                return False


                 
        

        elif(receptor_obj.organo == "Riñon izquierdo" or receptor_obj.organo == "Riñon derecho" or receptor_obj.organo == "Higado" or receptor_obj.organo == "Intestinos" or receptor_obj.organo == "Pancreas") and self.especialidad == "Gastroenterologo":


            random_num = random.randint(1,10) 


            if random_num >= 3 :                 
                return True 
            

            else:
                return False
        

        



        elif(receptor_obj.organo == "Pulmon izquierdo" or receptor_obj.organo == "Pulmon derecho") and self.especialidad == "Pulmonar" :


            random_num = random.randint(1,10)  



            if random_num >= 3 : 
                 return True 
            

            else :
                return False


        


        elif(receptor_obj.organo == "Piel" or receptor_obj.organo == "Corneas") and self.especialidad == "Plastico" :



            random_num = random.randint(1,10)  


            if random_num >= 3 :               
                return True 
            

            else :
                return False
            

        
        

        elif(receptor_obj.organo == "Hueso") and self.especialidad == "Traumatologo" :


            random_num = random.randint(1,10)  


            if random_num >= 3 : 
                return True 


            else :
                return False
            


        # UN CASO DIFERENTE :

        # cuando no se cumplen ninguno de los anteriores casos , determino la probabilidad de la cirujia con menor probabilidad de exito 


        else:


            random_num = random.randint(1,10)


            if random_num > 5 :
                return True
            

            else :
                return False




















