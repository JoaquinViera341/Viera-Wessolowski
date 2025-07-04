from abc import ABC, abstractclassmethod 
from haversine import haversine, Unit
import openrouteservice
from opencage.geocoder import OpenCageGeocode
from datetime import datetime, timedelta

opencage_key="a481e53b53dd484fb25862d831e8dafe"
geocoder = OpenCageGeocode(opencage_key)
openroute_key = "5b3ce3597851110001cf6248cb2d934504e04aa7820d8d023d860c48"
client = openrouteservice.Client(key=openroute_key)

class vehiculos (ABC):

    def __init__(self, velocidad : float, lista_viajes : list, lista_fecha_viajes : datetime, disponibilidad : bool, matricula : str):

        self.velocidad = velocidad

        self.lista_viajes = lista_viajes

        self.disponibilidad = disponibilidad 

        self.lista_fecha_viajes = lista_fecha_viajes

        self.matricula = matricula

        pass


    @abstractclassmethod

    def calcular_tiempo_viaje(self) :
        """ Este metodo abstracto es implementado  por las clases hijas para calcular el tiempo de viaje que hay de un centro de salud  a otro  """
        pass

    def imprimir_viajes(self):
        """ Este metodo abstracto es implementado por las clases hijas para imprimir los viajes realizados por el vehiculo """
        pass
    
    def liberar_vehiculo(self):
        """ Este metodo abstracto es implementado por las clases hijas para liberar el vehiculo y que este pueda ser utilizado nuevamente """
        self.disponibilidad = True
        return

class auto(vehiculos) :


    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)


        pass


    def calcular_tiempo_viaje(self, origen : str , destino: str )-> timedelta :


        """"Con la libreria geocoder convierto la direccion de los centros de salud en coordenadas geograficas (latitud y longitud)
        Luego con la libreria OpenRouteService obtengo la ruta entre los centros de salud y calcula el tiempo de viaje en minutos como si fuera google maps"""



        direccion_hospital_salida = geocoder.geocode(origen) # obtengo la direccion del centro de salud de origen

        if direccion_hospital_salida == None: # verifico que la direccion no sea none
            raise ValueError("No se pudo encontrar la dirección de origen") 
        else: # si la direccion existe y no es none , obtengo las coordenadas del centro de salud de origen ( latitud y longitud )
            latitud_salida = direccion_hospital_salida[0]['geometry']['lat'] # obtengo la latitud del centro de salud de origen 
            longitud_salida = direccion_hospital_salida[0]['geometry']['lng'] # obtengo la longitud del centro de salud de origen 

        direccion_hospital_destino = geocoder.geocode(destino) # obtengo la direccion del centro de salud de destino o llegada 

        if direccion_hospital_destino == None : # verifico que la direccion no sea none 

            raise ValueError("No se pudo encontrar la dirección de destino")
        
        else : # si la direccion existe y no es none , obtengo las coordenadas del centro de salud de destino o llegada ( latitud y longitud )

            latitud_destino = direccion_hospital_destino[0]['geometry']['lat'] # obtengo la latitud del centro de salud de destino 
            longitud_destino = direccion_hospital_destino[0]['geometry']['lng'] # obtengo la longitud del centro de salud de destino 


        #  me creo una tupla con las coordenadas de salida y otra con las coordenadas de destino
        cordenadas_salida = (latitud_salida, longitud_salida)
        cordenadas_destino = (latitud_destino, longitud_destino)


        ruta = client.directions(profile='driving-car',coordinates=[cordenadas_salida, cordenadas_destino],format='geojson') # obtengo la ruta entre el centro de salud de origen y el centro de salud de destino utilizando la libreria de OpenRouteService
        resumen = ruta['features'][0]['properties']['segments'][0]  # obtengo el resumen de la ruta que contiene la duracion del viaje en segundos 
        tiempo_viaje = timedelta(seconds=resumen['duration'])  # convierto el tiempo de viaje a minutos


        self.lista_viajes.append((origen, destino)) # agrego el viaje a la lista de viajes del vehiculo
        self.lista_fecha_viajes.append(datetime.now()) # agrego la fecha del viaje a la lista de fechas de viajes del vehiculo
        self.disponibilidad = False # el vehiculo ya no esta disponible para ser utilizado
        return tiempo_viaje # devuelvo el tiempo de viaje en minutos
    

    def __str__(self) -> str:
        """ Este metodo devuelve una presentacion basica del vehiculo """
        if self.disponibilidad == True:
            disponibilidad = "Disponible"
        else: 
            disponibilidad = "No disponible"
        if self.lista_viajes and self.lista_fecha_viajes:
            viajes_info = "\n".join(
            [f"  - {origen} -> {destino} en {fecha.strftime('%d/%m/%Y %H:%M')}"
             for (origen, destino), fecha in zip(self.lista_viajes, self.lista_fecha_viajes)]
        )
        else:
            viajes_info = "No se registraron viajes."
        text = (
            f"Vehiculo: Auto \n"
            f"Matricula: {self.matricula} \n"
            f"Velocidad: {self.velocidad} km/h \n"
            f"Disponibilidad: {disponibilidad} \n"
            f"Viajes realizados: \n{viajes_info}"
        )


class avion(vehiculos) :


    def __init__(self , velocidad : float , lista_viajes : list , disponibilidad : bool ) :
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass



    def calcular_tiempo_viaje(self, origen : str , destino : str) -> timedelta :
        """Con openCage Geocoder convierto la direccion de los centros de salud en coordenadas geograficas (latitud y longitud)
        Con Haversine calculo la distancia entre los centros en Km
        Calculo en base a la velocidad del avion y la distancia el tiempo de viaje"""
        
        direccion_hospital_salida = geocoder.geocode(origen) # obtengo la direccion del centro de salud de origen 


        if direccion_hospital_salida == None : # verifico que la direccion no sea none 

            raise ValueError("No se pudo encontrar la dirección de origen")
        
        else: # si la direccion existe y no es none , obtengo las coordenadas del centro de salud de origen ( latitud y longityud )


            latitud_salida = direccion_hospital_salida[0]['geometry']['lat'] # obtengo la latitud del centro de salud de origen
            longitud_salida = direccion_hospital_salida[0]['geometry']['lng'] # obtengo la longitud del centro de salud de origen



        direccion_hospital_destino = geocoder.geocode(destino) # obtengo la direccion del centro de salud de destino o llegada

        if direccion_hospital_destino == None : # verifico que la direccion no sea none

            raise ValueError("No se pudo encontrar la dirección de destino")
        
        else :

            latitud_destino = direccion_hospital_destino[0]['geometry']['lat'] # obtengo la latitud del centro de salud de destino
            longitud_destino = direccion_hospital_destino[0]['geometry']['lng'] # obtengo la longitud del centro de salud de destino
        
        cordenadas_salida = (latitud_salida, longitud_salida) # me creo una tupla con las coordenadas de salida
        cordenadas_destino = (latitud_destino, longitud_destino) # me creo una tupla con las coordenadas de destino

         
        # importante : la libreria haversine calcula la distancia entre dos puntos geograficos en km 

        distancia_km = haversine(cordenadas_salida, cordenadas_destino, unit=Unit.KILOMETERS)

        horas = distancia_km / self.velocidad # calculo el tiempo de viaje en horas dividiendo la distancia en km por la velocidad del avion en km/h
        tiempo_viaje = timedelta(hours=horas)
        self.lista_viajes.append((origen, destino)) # agrego el viaje a la lista de viajes del vehiculo

        self.lista_fecha_viajes.append(datetime.now()) # agrego la fecha del viaje a la lista de fechas de viajes del vehiculo

        self.disponibilidad = False # el vehiculo ya no esta disponible para ser utilizado

        return tiempo_viaje  
    


    def __str__(self) -> str:
        """ Este metodo devuelve una presentacion basica del vehiculo """
        if self.disponibilidad == True:
            disponibilidad = "Disponible"
        else: 
            disponibilidad = "No disponible"
        if self.lista_viajes and self.lista_fecha_viajes:
            viajes_info = "\n".join(
            [f"  - {origen} -> {destino} en {fecha.strftime('%d/%m/%Y %H:%M')}"
             for (origen, destino), fecha in zip(self.lista_viajes, self.lista_fecha_viajes)]
        )
        else:
            viajes_info = "No se registraron viajes."
        text = (
            f"Vehiculo: Avion \n"
            f"Matricula: {self.matricula} \n"
            f"Velocidad: {self.velocidad} km/h \n"
            f"Disponibilidad: {disponibilidad} \n"
            f"Viajes realizados: \n{viajes_info}"
        )



class helicoptero(vehiculos) :


    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass

    def calcular_tiempo_viaje(self, origen : str , destino : str) -> datetime :

        """ Calcula el tiempo de viaje del helicoptero que hay de un punto a otra """


        direccion_hospital_salida = geocoder.geocode(origen) # obtengo la direccion del centro de salud de origen

        if direccion_hospital_salida == None : # verifico que la direccion no sea none
            raise ValueError("No se pudo encontrar la dirección de origen")
        else : # si la direccion existe y no es none , obtengo las coordenadas del centro de salud de origen ( latitud y longitud )
            latitud_salida = direccion_hospital_salida[0]['geometry']['lat'] # obtengo la latitud del centro de salud de origen
            longitud_salida = direccion_hospital_salida[0]['geometry']['lng'] # obtengo la longitud del centro de salud de origen

        direccion_hospital_destino = geocoder.geocode(destino) # obtengo la direccion del centro de salud de destino o llegada

        if direccion_hospital_destino == None : # verifico que la direccion no sea none

            raise ValueError("No se pudo encontrar la dirección de destino")
        
        else: # si la direccion existe y no es none , obtengo las coordenadas del centro de salud de destino o llegada ( latitud y longitud )

            latitud_destino = direccion_hospital_destino[0]['geometry']['lat'] # obtengo la latitud del centro de salud de destino
            longitud_destino = direccion_hospital_destino[0]['geometry']['lng'] # obtengo la longitud del centro de salud de destino
        

        cordenadas_salida = (latitud_salida, longitud_salida) # me creo una tupla con las coordenadas de salida
        cordenadas_destino = (latitud_destino, longitud_destino) # me creo una tupla con las coordenadas de destino



        # importante : la libreria haversine calcula la distancia entre dos puntos geograficos en km
        distancia_km = haversine(cordenadas_salida, cordenadas_destino, unit=Unit.KILOMETERS)


        horas = distancia_km / self.velocidad # calculo el tiempo de viaje en horas dividiendo la distancia en km por la velocidad del helicoptero en km/h
        tiempo_viaje = timedelta(hours=horas)
        self.lista_viajes.append((origen, destino)) # agrego el viaje a la lista de viajes del vehiculo

        self.lista_fecha_viajes.append(datetime.now()) # agrego la fecha del viaje a la lista de fechas de viajes del vehiculo

        self.disponibilidad = False # el vehiculo ya no esta disponible para ser utilizado

        return tiempo_viaje
    

    
    def __str__(self) -> str :
        
        """ Este metodo devuelve una presentacion basica del vehiculo """
        if self.disponibilidad == True:
            disponibilidad = "Disponible"
        else: 
            disponibilidad = "No disponible"
        if self.lista_viajes and self.lista_fecha_viajes:
            viajes_info = "\n".join(
            [f"  - {origen} -> {destino} en {fecha.strftime('%d/%m/%Y %H:%M')}"
             for (origen, destino), fecha in zip(self.lista_viajes, self.lista_fecha_viajes)]
        )
        else:
            viajes_info = "No se registraron viajes."
        text = (
            f"Vehiculo: helicoptero \n"
            f"Matricula: {self.matricula} \n"
            f"Velocidad: {self.velocidad} km/h \n"
            f"Disponibilidad: {disponibilidad} \n"
            f"Viajes realizados: \n{viajes_info}"
        )
    
