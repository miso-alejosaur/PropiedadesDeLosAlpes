import typing
import strawberry
import uuid
import requests
import os
from pulsar.schema import *
from src.bff_investigacion import utils

COREANALITICA_ADDRESS = os.getenv("COREANALITICA_ADDRESS", default="localhost")
ID="Colombia"

def obtener_promedio(name):
    print(name)
    
    metrica_json = requests.get(f'http://{COREANALITICA_ADDRESS}:80/coreanalitica/obtener-metricas-pais/{name}').json()

    metrica = Metrica(
            pais=metrica_json["pais"], 
            valor_compra=metrica_json["valor_compra"], 
            valor_arrendamiento=metrica_json["valor_arrendamiento"]
            )

    return metrica

@strawberry.type
class Metrica:
    pais: str
    valor_compra: float
    valor_arrendamiento: float

@strawberry.type
class ConfiabilidadRespuesta:
    mensaje: str
    codigo: int

class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=utils.time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class EventoIntegracion(Mensaje):
    ...
    
class ComandoIntegracion(Mensaje):
    ...

class ActualizarIndiceConfiabilidadPayload(ComandoIntegracion):
    id_propiedad = String()
    indice_confiabilidad = Float()

class ComandoActualizarIndiceConfiabilidad(ComandoIntegracion):
    data = ActualizarIndiceConfiabilidadPayload()

class PropiedadDisponiblePayload(Record):
    id_propiedad = String()
    valor_compra = Float()
    valor_arrendamiento = Float()
    divisa = String()
    pais = String()
    indice_confiabilidad = Float()

class EventoPropiedadDisponible(EventoIntegracion):
    data = PropiedadDisponiblePayload()

class EventoIndiceActualizado(EventoIntegracion):
    data = PropiedadDisponiblePayload()