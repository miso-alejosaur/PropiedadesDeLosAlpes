import pulsar
from pulsar.schema import *
from src.auditoria.modulos.sagas.infraestructura.schema.v1.comandos import ComandoActualizarIndiceConfiabilidad, ActualizarIndiceConfiabilidadPayload, ComandoActualizarValoresPayload, ActualizarValoresPayload
from src.auditoria.seedwork.infraestructura import utils

import datetime

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topic=topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando(self, comando, topico, tipo_comando):
        if tipo_comando == ComandoActualizarIndiceConfiabilidad:
            payload = ActualizarIndiceConfiabilidadPayload(
                id_propiedad=str(comando.id_propiedad),
                indice_confiabilidad=float(comando.indice_confiabilidad),
                compensacion=int(1 if comando.compensacion else 0)
            )
            comando_integracion = ComandoActualizarIndiceConfiabilidad(data=payload)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoActualizarIndiceConfiabilidad))
        elif tipo_comando == ComandoActualizarValoresPayload:
            payload = ActualizarValoresPayload(
                id_pais=str(comando.pais),
                valor_arrendamiento=float(comando.valor_arrendamiento),
                valor_compra=float(comando.valor_compra),
                id_propiedad=str(comando.id_propiedad),
                indice_confiabilidad=float(comando.indice_confiabilidad)
            )
            comando_integracion = ComandoActualizarValoresPayload(data=payload)
            self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoActualizarValoresPayload))