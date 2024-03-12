import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from pydispatch import dispatcher

from src.auditoria.modulos.sagas.infraestructura.schema.v1.eventos import EventoContrato, EventoPropiedadDisponible, EventoMetricaDisponible
from src.auditoria.seedwork.infraestructura import utils
from src.auditoria.modulos.sagas.dominio.eventos.contratos import ContratoCreado
from src.auditoria.modulos.sagas.dominio.eventos.propiedades import IndiceConfiabilidadActualizado
from src.auditoria.modulos.sagas.dominio.eventos.metricas import PromediosValoresActualizados, PromediosActualizacionFallida


def suscribirse_a_eventos_contrato_creado(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-contratos-auditoria', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoContrato))

        while True:
            mensaje = consumidor.receive()
            data: EventoContrato = mensaje.value().data
            print(f'Evento recibido: {data}')
            with app.app_context():
                if data.exito == 1:
                    evento = ContratoCreado(id_contrato=data.id_contrato, valor=data.valor, valor_abonado=data.valor_abonado,fecha_inicio=data.fecha_inicio,
                                            fecha_vencimiento=data.fecha_vencimiento,
                                            pais=data.pais,
                                            divisa=data.divisa,
                                            tipo_contrato=data.tipo_contrato,
                                            id_propiedad=data.id_propiedad,
                                            id_correlacion=0)
                    dispatcher.send(signal=f'Saga', mensaje=evento)

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_indice_actualizado(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-auditoria-integracion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoPropiedadDisponible))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            comando = mensaje.value().data
            
            with app.app_context():
                if comando.exito == 1:
                    evento = IndiceConfiabilidadActualizado(id_propiedad=comando.id_propiedad, 
                                                            valor_compra=comando.valor_compra, 
                                                            valor_arrendamiento=comando.valor_arrendamiento, 
                                                            divisa=comando.divisa,
                                                            pais=comando.pais,
                                                            indice_confiabilidad=comando.indice_confiabilidad,
                                                            id_correlacion=0)
                    dispatcher.send(signal=f'Saga', mensaje=evento)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_metricas_actualizado(app):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-core', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='pda-sub-eventos', schema=AvroSchema(EventoMetricaDisponible))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            comando = mensaje.value().data
            
            with app.app_context():
                print('@@@@@@@@@@@@@@@@@ ', comando.exito)
                if comando.exito == 1:
                    evento = PromediosValoresActualizados(id_propiedad=comando.id_propiedad, 
                                                            valor_compra=comando.valor_compra, 
                                                            valor_arrendamiento=comando.valor_arrendamiento, 
                                                            pais=comando.pais,
                                                            id_correlacion=0)
                    dispatcher.send(signal=f'Saga', mensaje=evento)
                else: 
                    
                    evento = PromediosActualizacionFallida(id_propiedad=comando.id_propiedad, 
                                                            valor_compra=comando.valor_compra, 
                                                            valor_arrendamiento=comando.valor_arrendamiento, 
                                                            pais=comando.pais,
                                                            id_correlacion=0, indice_confiabilidad=comando.indice_confiabilidad)
                    dispatcher.send(signal=f'Saga', mensaje=evento)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()