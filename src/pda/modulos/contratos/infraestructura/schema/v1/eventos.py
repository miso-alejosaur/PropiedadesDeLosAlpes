from pulsar.schema import *

from src.pda.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class TransaccionCreadaPayload(Record):
    id_transaccion = String()
    valor = Float()
    fecha = String()
    divisa = String()
    contrato = String()

class EventoTransaccionCreada(EventoIntegracion):
    data = TransaccionCreadaPayload()

class AbonoContratoActualizadoPayload(Record):
    id_contrato = String()
    valor = Float()
    valor_abonado = Float()
    divisa = String()

class EventoAbonoContratoActualizado(EventoIntegracion):
    data = AbonoContratoActualizadoPayload()