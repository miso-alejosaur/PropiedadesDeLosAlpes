from pulsar.schema import *

from src.auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadDisponiblePayload(Record):
    id_propiedad = String()
    valor_compra = Float()
    valor_arrendamiento = Float()
    divisa = String()
    pais = String()
    indice_confiabilidad = Float()

class EventoPropiedadDisponible(EventoIntegracion):
    data = PropiedadDisponiblePayload()

class ContratoCreadoPayload(Record):
    id_contrato = String()
    valor = Float()
    valor_abonado = Float()
    fecha_inicio = String()
    fecha_vencimiento = String()
    pais = String()
    divisa = String()
    tipo_contrato = Integer()
    id_propiedad = String()

class EventoContratoCreado(EventoIntegracion):
    data = ContratoCreadoPayload()