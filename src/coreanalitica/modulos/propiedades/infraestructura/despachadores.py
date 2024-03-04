import pulsar
from pulsar.schema import *
from src.coreanalitica.modulos.propiedades.infraestructura.schema.v1.eventos import EventoMetricaDisponible, MetricaDisponiblePayload
from src.coreanalitica.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoActualizarValoresPayload, ActualizarValoresPayload
from src.coreanalitica.seedwork.infraestructura import utils

import datetime

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topic=topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = MetricaDisponiblePayload(
            id_paise=str(evento.id_propiedad),
            valor_compra=float(evento.valor_compra),
            valor_arrendamiento=float(evento.valor_arrendamiento),
            pais=str(evento.pais)
            )
        evento_integracion = EventoMetricaDisponible(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoMetricaDisponible))

    def publicar_comando(self, metrica, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = Ac(
            id_pais=str(metrica.id_metrica),
            valor_arrendamiento=float(metrica.valor_arrendamiento),
            valor_compra=float(metrica.valor_compra)
        )
        comando_integracion = ActualizarValoresPayload(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoActualizarValoresPayload))