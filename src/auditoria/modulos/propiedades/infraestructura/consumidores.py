import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from pydispatch import dispatcher

from src.auditoria.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadDisponible
from src.auditoria.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoActualizarIndiceConfiabilidad
from src.auditoria.seedwork.infraestructura.comandos import ejecutar_commando
from src.auditoria.seedwork.infraestructura import utils
from src.auditoria.modulos.propiedades.infraestructura.comandos.actualizar_indice_confiabilidad import ActualizarIndiceConfiabilidad
from src.auditoria.modulos.propiedades.infraestructura.despachadores import Despachador
from src.auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-contratos-auditoria', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoPropiedadDisponible))

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
        consumidor = cliente.subscribe('comandos-auditoria', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoActualizarIndiceConfiabilidad))
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comando = mensaje.value().data
            comando_contrato = ActualizarIndiceConfiabilidad(id_propiedad=comando.id_propiedad, indice_confiabilidad=comando.indice_confiabilidad)
            with app.app_context():
                    ejecutar_commando(comando_contrato)
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()