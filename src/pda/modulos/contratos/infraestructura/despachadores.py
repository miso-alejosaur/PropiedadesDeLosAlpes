import pulsar
from pulsar.schema import *
from src.pda.modulos.contratos.infraestructura.schema.v1.eventos import EventoAbonoContratoActualizado, AbonoContratoActualizadoPayload, EventoContrato, ContratoPayload
from src.pda.modulos.contratos.infraestructura.schema.v1.comandos import ComandoActualizarAbonoContrato, ComandoActualizarAbonoContratoPayload, ComandoCrearContrato, CrearContratoPayload
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
        payload = ContratoPayload(
            id_contrato=str(evento.id_contrato),
            valor=float(evento.valor),
            valor_abonado=float(evento.valor_abonado),
            divisa=str(evento.divisa),
            fecha_inicio=str(evento.fecha_inicio),
            fecha_vencimiento=str(evento.fecha_vencimiento),
            pais=str(evento.pais),
            tipo_contrato=int(evento.tipo_contrato),
            id_propiedad=str(evento.id_propiedad),
            exito=1
            )
        evento_integracion = EventoContrato(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoContrato))

    def publicar_comando(self, comando, topico):
        comando_integracion = None
        schema = None
        if topico == 'comandos-contrato':
            payload = ComandoActualizarAbonoContratoPayload(
                valor_abonado=float(comando.valor_abonado),
                id_contrato=str(comando.id_contrato)
            )
            comando_integracion = ComandoActualizarAbonoContrato(data=payload)
            schema = AvroSchema(ComandoActualizarAbonoContrato)
        elif topico == 'comandos-crear-contrato':
            payload = CrearContratoPayload(
                valor = float(comando.valor),
                valor_abonado = float(comando.valor_abonado),
                fecha_inicio = str(comando.fecha_inicio),
                fecha_vencimiento = str(comando.fecha_vencimiento),
                pais = str(comando.pais),
                divisa = str(comando.divisa),
                tipo_contrato = int(comando.tipo_contrato),
                id_propiedad = str(comando.id_propiedad)
            )
            comando_integracion = ComandoCrearContrato(data=payload)
            schema = AvroSchema(ComandoCrearContrato)
        self._publicar_mensaje(comando_integracion, topico, schema)