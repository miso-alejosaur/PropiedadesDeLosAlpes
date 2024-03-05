from pulsar.schema import *

from src.coreanalitica.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class MetricaDisponiblePayload(Record):
    id = String()
    valor_compra = Float()
    valor_arrendamiento = Float()
    pais = String()

class EventoMetricaDisponible(EventoIntegracion):
    data = MetricaDisponiblePayload()


class PropiedadDisponiblePayload(Record):
    id_propiedad = String()
    valor_compra = Float()
    valor_arrendamiento = Float()
    divisa = String()
    pais = String()
    indice_confiabilidad = Float()

class EventoPropiedadDisponible(EventoIntegracion):
    data = PropiedadDisponiblePayload()