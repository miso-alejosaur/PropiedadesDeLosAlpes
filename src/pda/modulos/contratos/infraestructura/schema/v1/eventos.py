from pulsar.schema import *

from src.pda.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ContratoPayload(Record):
    id_contrato = String()
    valor = Float()
    valor_abonado = Float()
    fecha_inicio = String()
    fecha_vencimiento = String()
    pais = String()
    divisa = String()
    tipo_contrato = Integer()
    id_propiedad = String()
    exito = Integer()

class EventoContrato(EventoIntegracion):
    data = ContratoPayload()

class AbonoContratoActualizadoPayload(Record):
    id_contrato = String()
    valor = Float()
    valor_abonado = Float()
    divisa = String()

class EventoAbonoContratoActualizado(EventoIntegracion):
    data = AbonoContratoActualizadoPayload()

class TransaccionCreadaPayload(Record):
    id_transaccion = String()
    valor = Float()
    fecha = String()
    divisa = String()
    contrato = String()

class EventoTransaccionCreada(EventoIntegracion):
    data = TransaccionCreadaPayload()