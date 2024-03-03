import pulsar
from pulsar.schema import *
from src.pda.modulos.contratos.infraestructura.schema.v1.eventos import EventoAbonoContratoActualizado, AbonoContratoActualizadoPayload
from src.pda.modulos.contratos.infraestructura.schema.v1.comandos import ComandoActualizarAbonoContrato, ComandoActualizarAbonoContratoPayload
from src.pda.seedwork.infraestructura import utils

import datetime

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topic=topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = AbonoContratoActualizadoPayload(
            id_contrato=str(evento.id_contrato),
            valor=float(evento.valor),
            valor_abonado=float(evento.valor_abonado),
            divisa=str(evento.divisa)
            )
        evento_integracion = EventoAbonoContratoActualizado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoAbonoContratoActualizado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoActualizarAbonoContratoPayload(
            valor_abonado=float(comando.valor_abonado),
            id_contrato=str(comando.id_contrato)
        )
        comando_integracion = ComandoActualizarAbonoContrato(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoActualizarAbonoContrato))