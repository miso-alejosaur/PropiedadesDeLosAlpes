import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.pda.modulos.contratos.infraestructura.schema.v1.eventos import EventoTransaccionCreada
from src.pda.modulos.contratos.infraestructura.schema.v1.comandos import ComandoActualizarAbonoContrato, ComandoCrearContrato
from src.pda.seedwork.infraestructura.comandos import ejecutar_commando
from src.pda.seedwork.infraestructura import utils
from src.pda.modulos.contratos.infraestructura.comandos.actualizar_abono_contrato import ActualizarAbonoContrato
from src.pda.modulos.contratos.infraestructura.comandos.crear_contrato import CrearContrato
from src.pda.modulos.contratos.infraestructura.despachadores import Despachador
from src.pda.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-transaccion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoTransaccionCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            
            comando = mensaje.value().data
            transaccion_valor, id_contrato = comando.valor, comando.contrato
            comando_contrato = ActualizarAbonoContrato(valor_abonado=transaccion_valor, id_contrato=id_contrato)
            despachador = Despachador()
            despachador.publicar_comando(comando=comando_contrato, topico='comandos-contrato')
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
        consumidor = cliente.subscribe('comandos-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoActualizarAbonoContrato))
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comando = mensaje.value().data
            comando_contrato = ActualizarAbonoContrato(valor_abonado=comando.valor_abonado, id_contrato=comando.id_contrato)
            with app.app_context():
                    ejecutar_commando(comando_contrato)
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_crear(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-crear-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoCrearContrato))
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comando = mensaje.value().data
            comando_contrato = CrearContrato(valor=comando.valor, valor_abonado=comando.valor_abonado, fecha_inicio=comando.fecha_inicio,
                                                    fecha_vencimiento=comando.fecha_vencimiento, tipo_contrato=comando.tipo_contrato, pais=comando.pais,
                                                    divisa=comando.divisa, id_propiedad=comando.id_propiedad)
            with app.app_context():
                    ejecutar_commando(comando_contrato)
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()