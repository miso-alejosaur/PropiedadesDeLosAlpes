from pulsar.schema import *

class EventoIntegracion(Mensaje):
    ...
    
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
    