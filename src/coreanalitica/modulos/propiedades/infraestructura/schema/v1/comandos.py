from pulsar.schema import *
from dataclasses import dataclass, field
from src.coreanalitica.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ActualizarValoresPayload(ComandoIntegracion):
    id_pais = String()
    valor_arrendamiento = Float()
    valor_compra = Float()

class ComandoActualizarValoresPayload(ComandoIntegracion):
    data = ActualizarValoresPayload()