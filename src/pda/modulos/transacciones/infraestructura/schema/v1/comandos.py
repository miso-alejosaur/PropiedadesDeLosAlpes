from pulsar.schema import *
from dataclasses import dataclass, field
from src.pda.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearTransaccionPayload(ComandoIntegracion):
    valor = Float()
    fecha = String()
    divisa = String()
    contrato = String()

class ComandoCrearTransaccion(ComandoIntegracion):
    data = ComandoCrearTransaccionPayload()