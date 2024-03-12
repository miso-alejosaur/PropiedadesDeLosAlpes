from pydispatch import dispatcher

from src.auditoria.modulos.sagas.aplicacion.coordinadores.saga_propiedades import HandlerSagasDominio

dispatcher.connect(HandlerSagasDominio.oir_mensaje, signal=f'Saga')
