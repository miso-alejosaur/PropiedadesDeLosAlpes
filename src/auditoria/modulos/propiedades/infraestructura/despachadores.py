import pulsar
from pulsar.schema import *
from src.auditoria.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadDisponible, PropiedadDisponiblePayload
from src.auditoria.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoActualizarIndiceConfiabilidad, ActualizarIndiceConfiabilidadPayload
from src.auditoria.seedwork.infraestructura import utils

import datetime

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topic=topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadDisponiblePayload(
            id_propiedad=str(evento.id_propiedad),
            valor_compra=float(evento.valor_compra),
            valor_arrendamiento=float(evento.valor_arrendamiento),
            divisa=str(evento.divisa),
            pais=str(evento.pais),
            indice_confiabilidad=float(evento.indice_confiabilidad),
            exito=int(evento.exito)
            )
        evento_integracion = EventoPropiedadDisponible(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPropiedadDisponible))

    def publicar_comando(self, propiedad, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ActualizarIndiceConfiabilidadPayload(
            id_propiedad=str(propiedad.id_propiedad),
            indice_confiabilidad=float(propiedad.indice_confiabilidad)
        )
        comando_integracion = ComandoActualizarIndiceConfiabilidad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoActualizarIndiceConfiabilidad))