from pulsar.schema import *
from dataclasses import dataclass, field
from src.pda.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoActualizarAbonoContratoPayload(ComandoIntegracion):
    valor_abonado = Float()
    id_contrato = String()

class ComandoActualizarAbonoContrato(ComandoIntegracion):
    data = ComandoActualizarAbonoContratoPayload()