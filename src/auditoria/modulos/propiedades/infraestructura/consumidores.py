import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from pydispatch import dispatcher

from src.auditoria.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadDisponible, EventoContrato
from src.auditoria.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoActualizarIndiceConfiabilidad
from src.auditoria.seedwork.infraestructura.comandos import ejecutar_commando
from src.auditoria.seedwork.infraestructura import utils
from src.auditoria.modulos.propiedades.infraestructura.comandos.actualizar_indice_confiabilidad import ActualizarIndiceConfiabilidad
from src.auditoria.modulos.propiedades.infraestructura.despachadores import Despachador
from src.auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from src.auditoria.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from src.auditoria.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from src.auditoria.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from src.auditoria.modulos.propiedades.dominio.entidades import Propiedad
from src.auditoria.seedwork.dominio.eventos import EventoDominio, EventoIntegracion

def suscribirse_a_eventos(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-contratos-auditoria2', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoContrato))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            with app.app_context():
                fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
                repositorio = fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
                propiedad: Propiedad = repositorio.actualizar_propiedad(mensaje.value().data)
                propiedad.actualizar_indice_confiabilidad(propiedad)
                for evento in propiedad.eventos:
                    if isinstance(evento, EventoDominio):
                        print(evento, f'{type(evento).__name__}Dominio')
                        dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
                    elif isinstance(evento, EventoIntegracion):
                        print(evento, f'{type(evento).__name__}Integracion')
                        dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)

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
            comando_contrato = ActualizarIndiceConfiabilidad(id_propiedad=comando.id_propiedad, indice_confiabilidad=comando.indice_confiabilidad, compensacion=(True if comando.compensacion == 1 else False))
            with app.app_context():
                    ejecutar_commando(comando_contrato)
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()