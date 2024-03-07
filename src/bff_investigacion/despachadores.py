import pulsar
from pulsar.schema import *

from . import utils

class Despachador:
    def __init__(self):
        ...

    async def publicar_mensaje(self, mensaje, topico, schema):

        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer("", schema=AvroSchema())
        publicador.send(mensaje)
        cliente.close()