import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from pydispatch import dispatcher

from src.coreanalitica.modulos.propiedades.infraestructura.schema.v1.eventos import EventoMetricaDisponible
from src.coreanalitica.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoActualizarValoresPayload
from src.coreanalitica.seedwork.infraestructura.comandos import ejecutar_commando
from src.coreanalitica.seedwork.infraestructura import utils
from src.coreanalitica.modulos.propiedades.infraestructura.comandos.actualizar_promedios import ActualizarPromedios
from src.coreanalitica.modulos.propiedades.infraestructura.despachadores import Despachador
from src.coreanalitica.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-auditoria-integracion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoMetricaDisponible))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            
            #TODO recibir contrato
            #dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-metricas', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoActualizarIndiceConfiabilidad))
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comando = mensaje.value().data
            comando_contrato = ActualizarPromedios(id_pais=comando.id_pais, valor_arrendamiento=comando.valor_arrendamiento, valor_compra=comando.valore_compra
            )
            with app.app_context():
                    ejecutar_commando(comando_contrato)
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()