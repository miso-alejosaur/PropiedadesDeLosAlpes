from pulsar.schema import *
from dataclasses import dataclass, field
from src.pda.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoActualizarAbonoContratoPayload(ComandoIntegracion):
    valor_abonado = Float()
    id_contrato = String()

class ComandoActualizarAbonoContrato(ComandoIntegracion):
    data = ComandoActualizarAbonoContratoPayload()

class CrearContratoPayload(ComandoIntegracion):
    valor = Float()
    valor_abonado = Float()
    fecha_inicio = String()
    fecha_vencimiento = String()
    pais = String()
    divisa = String()
    tipo_contrato = Integer()
    id_propiedad = String()

class ComandoCrearContrato(ComandoIntegracion):
    data = CrearContratoPayload()