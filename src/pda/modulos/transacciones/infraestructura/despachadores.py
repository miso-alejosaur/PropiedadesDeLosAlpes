import pulsar
from pulsar.schema import *

from src.pda.modulos.transacciones.infraestructura.schema.v1.eventos import EventoTransaccionCreada, TransaccionCreadaPayload
from src.pda.modulos.transacciones.infraestructura.schema.v1.comandos import ComandoCrearTransaccion, ComandoCrearTransaccionPayload
from src.pda.seedwork.infraestructura import utils

import datetime

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoTransaccionCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = TransaccionCreadaPayload(
            id_transaccion=str(evento.id_transaccion),
            valor=float(evento.valor.monto),
            fecha=str(evento.fecha),
            divisa=str(evento.divisa),
            contrato=str(evento.contrato)
        )
        evento_integracion = EventoTransaccionCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoTransaccionCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearTransaccionPayload(
            valor=float(comando.valor),
            fecha=str(comando.fecha),
            hora=str(comando.hora),
            divisa=str(comando.divisa),
            contrato=str(comando.contrato)
        )
        comando_integracion = ComandoCrearTransaccion(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearTransaccion))