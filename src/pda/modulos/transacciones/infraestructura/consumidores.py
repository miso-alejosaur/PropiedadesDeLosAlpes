import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from src.pda.modulos.transacciones.infraestructura.schema.v1.eventos import EventoTransaccionCreada
from src.pda.modulos.transacciones.infraestructura.schema.v1.comandos import ComandoCrearTransaccion
from src.pda.seedwork.aplicacion.comandos import ejecutar_commando
from src.pda.seedwork.infraestructura import utils
from src.pda.modulos.transacciones.aplicacion.comandos.crear_transaccion import CrearTransaccion

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-transaccion-interno', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoTransaccionCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

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
        consumidor = cliente.subscribe('comandos-transaccion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='pda-sub-comandos', schema=AvroSchema(ComandoCrearTransaccion))
        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')
            comando = mensaje.value().data
            transaccion = CrearTransaccion(comando.valor, comando.fecha, comando.divisa, comando.contrato)
            with app.app_context():
                ejecutar_commando(transaccion)

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()