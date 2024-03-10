import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from utils import *

async def suscribirse_a_topico(suscripcion: str, eventos=[]):
    try:
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                suscripcion, 
                consumer_type=_pulsar.ConsumerType.Shared,
                subscription_name='pda-sub-eventos', 
                schema=AvroSchema(EventoPropiedadDisponible)
            ) as consumidor:
                print(f'ya me suscribi')
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos}')
                    eventos.append(str(datos))
                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}, {schema}')
        traceback.print_exc()

async def suscribirse_a_eventos(app):
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-auditoria-integracion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoPropiedadDisponible))

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