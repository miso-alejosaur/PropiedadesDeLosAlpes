from pulsar.schema import *
from dataclasses import dataclass, field
from src.auditoria.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ActualizarIndiceConfiabilidadPayload(ComandoIntegracion):
    id_propiedad = String()
    indice_confiabilidad = Float()
    compensacion = Integer()

class ComandoActualizarIndiceConfiabilidad(ComandoIntegracion):
    data = ActualizarIndiceConfiabilidadPayload()


class ActualizarValoresPayload(ComandoIntegracion):
    id_pais = String()
    valor_arrendamiento = Float()
    valor_compra = Float()
    id_propiedad = String()
    indice_confiabilidad = Float()

class ComandoActualizarValoresPayload(ComandoIntegracion):
    data = ActualizarValoresPayload()