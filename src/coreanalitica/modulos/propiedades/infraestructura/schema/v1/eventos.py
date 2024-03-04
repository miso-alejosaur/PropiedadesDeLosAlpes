from pulsar.schema import *

from src.coreanalitica.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class MetricaDisponiblePayload(Record):
    id_pais = String()
    valor_compra = Float()
    valor_arrendamiento = Float()()
    pais = String()

class EventoMetricaDisponible(EventoIntegracion):
    data = MetricaDisponiblePayload()