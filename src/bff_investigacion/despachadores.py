import pulsar
from pulsar.schema import *

from . import utils
from src.bff_investigacion.api.v1.esquemas import ComandoActualizarIndiceConfiabilidad

class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoActualizarIndiceConfiabilidad))
        publicador.send(mensaje)
        cliente.close()