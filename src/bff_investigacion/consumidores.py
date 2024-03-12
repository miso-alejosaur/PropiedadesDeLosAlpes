import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from utils import *
from src.bff_investigacion.api.v1.esquemas import EventoPropiedadDisponible

async def suscribirse_a_topico(suscripcion: str, eventos=[]):
    try:
        async with aiopulsar.connect(f'pulsar://{broker_host()}:6650') as cliente:
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
                    datos = mensaje.value().data
                    print(f'Evento recibido: {datos}')
                    eventos.append(str(datos))
                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error(f'ERROR: Suscribiendose al tópico! {topico}, {suscripcion}, {schema}')
        traceback.print_exc()