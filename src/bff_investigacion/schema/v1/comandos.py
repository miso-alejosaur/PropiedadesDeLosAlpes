from pulsar.schema import *
from dataclasses import dataclass, field
from src.auditoria.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ActualizarIndiceConfiabilidadPayload(ComandoIntegracion):
    id_propiedad = String()
    indice_confiabilidad = Float()

class ComandoActualizarIndiceConfiabilidad(ComandoIntegracion):
    data = ActualizarIndiceConfiabilidadPayload()