from abc import ABC, abstractclassmethod 
from haversine import haversine, Unit
import openrouteservice
from opencage.geocoder import OpenCageGeocode
from datetime import datetime

opencage_key="a481e53b53dd484fb25862d831e8dafe"
geocoder = OpenCageGeocode(opencage_key)
openroute_key = "5b3ce3597851110001cf6248cb2d934504e04aa7820d8d023d860c48"
client = openrouteservice.Client(key=openroute_key)


class vehiculos (ABC):

    def __init__(self, velocidad : float, lista_viajes : list, lista_fecha_viajes : datetime, disponibilidad : bool, matricula : str):

        self.velocidad = velocidad

        self.lista_viajes = lista_viajes

        self.disponibilidad = disponibilidad #si el vehiculo esta disponible es True , si no es false

        self.lista_fecha_viajes = lista_fecha_viajes

        self.matricula = matricula

    @abstractclassmethod

    def calcular_tiempo_viaje(self, origen : str, destino : str) -> float:
        return

    def imprimir_viajes(self):
        return
    
    def liberar_vehiculo(self):
        self.disponibilidad = True
        return

class auto(vehiculos):
    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass

    def calcular_tiempo_viaje(self, origen, destino):
        direccion_hospital_salida = geocoder.geocode(origen)
        if direccion_hospital_salida == None:
            raise ValueError("No se pudo encontrar la dirección de origen")
        else:
            latitud_salida = direccion_hospital_salida[0]['geometry']['lat']
            longitud_salida = direccion_hospital_salida[0]['geometry']['lng']

        direccion_hospital_destino = geocoder.geocode(destino)
        if direccion_hospital_destino == None:
            raise ValueError("No se pudo encontrar la dirección de destino")
        else:
            latitud_destino = direccion_hospital_destino[0]['geometry']['lat']
            longitud_destino = direccion_hospital_destino[0]['geometry']['lng']
        
        cordenadas_salida = (latitud_salida, longitud_salida)
        cordenadas_destino = (latitud_destino, longitud_destino)

        ruta= client.directions(
            profile='driving-car',
            coordinates=[cordenadas_salida, cordenadas_destino],
            format='geojson'
        )
        resumen = ruta['features'][0]['properties']['segments'][0]
        tiempo_viaje = resumen['duration'] / 60

        self.lista_viajes.append((origen, destino)) 
        self.lista_fecha_viajes.append(datetime.now())
        self.disponibilidad = False
        return tiempo_viaje
    
    def imprimir_viajes(self):
        for x in (1, len(self.lista_viajes)):
            print(f"Viaje de {x}: {self.lista_viajes[x-1][0]} a {self.lista_viajes[x-1][1]} el {self.lista_fecha_viajes[x-1]}")
        return

class avion(vehiculos):
    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass

    def calcular_tiempo_viaje(self, origen, destino):
        direccion_hospital_salida = geocoder.geocode(origen)
        if direccion_hospital_salida == None:
            raise ValueError("No se pudo encontrar la dirección de origen")
        else:
            latitud_salida = direccion_hospital_salida[0]['geometry']['lat']
            longitud_salida = direccion_hospital_salida[0]['geometry']['lng']

        direccion_hospital_destino = geocoder.geocode(destino)
        if direccion_hospital_destino == None:
            raise ValueError("No se pudo encontrar la dirección de destino")
        else:
            latitud_destino = direccion_hospital_destino[0]['geometry']['lat']
            longitud_destino = direccion_hospital_destino[0]['geometry']['lng']
        
        cordenadas_salida = (latitud_salida, longitud_salida)
        cordenadas_destino = (latitud_destino, longitud_destino)

        distancia_km = haversine(cordenadas_salida, cordenadas_destino, unit=Unit.KILOMETERS)
        tiempo_viaje = distancia_km / self.velocidad

        self.lista_viajes.append((origen, destino)) 
        self.lista_fecha_viajes.append(datetime.now())
        self.disponibilidad = False
        return tiempo_viaje
    def imprimir_viajes(self):
        for x in (1, len(self.lista_viajes)):
            print(f"Viaje de {x}: {self.lista_viajes[x-1][0]} a {self.lista_viajes[x-1][1]} el {self.lista_fecha_viajes[x-1]}")
        return


class helicoptero(vehiculos):
    def __init__(self, velocidad : float, lista_viajes : list, disponibilidad : bool):
        super().__init__(velocidad, lista_viajes, disponibilidad)

        pass

    def calcular_tiempo_viaje(self, origen, destino):
        direccion_hospital_salida = geocoder.geocode(origen)
        if direccion_hospital_salida == None:
            raise ValueError("No se pudo encontrar la dirección de origen")
        else:
            latitud_salida = direccion_hospital_salida[0]['geometry']['lat']
            longitud_salida = direccion_hospital_salida[0]['geometry']['lng']

        direccion_hospital_destino = geocoder.geocode(destino)
        if direccion_hospital_destino == None:
            raise ValueError("No se pudo encontrar la dirección de destino")
        else:
            latitud_destino = direccion_hospital_destino[0]['geometry']['lat']
            longitud_destino = direccion_hospital_destino[0]['geometry']['lng']
        
        cordenadas_salida = (latitud_salida, longitud_salida)
        cordenadas_destino = (latitud_destino, longitud_destino)

        distancia_km = haversine(cordenadas_salida, cordenadas_destino, unit=Unit.KILOMETERS)
        tiempo_viaje = distancia_km / self.velocidad

        self.lista_viajes.append((origen, destino)) 
        self.lista_fecha_viajes.append(datetime.now())
        self.disponibilidad = False
        return tiempo_viaje
    
    def imprimir_viajes(self):
        for x in (1, len(self.lista_viajes)):
            print(f"Viaje de {x}: {self.lista_viajes[x-1][0]} a {self.lista_viajes[x-1][1]} el {self.lista_fecha_viajes[x-1]}")
        return
    
