from pydispatch import dispatcher

from .handlers import HandlerMetricaDominio, HandlerMetricaIntegracion

from src.coreanalitica.modulos.propiedades.dominio.eventos import PromediosValoresActualizados

dispatcher.connect(HandlerMetricaIntegracion.handle_metrica_disponible, signal=f'{PromediosValoresActualizados.__name__}Integracion')
dispatcher.connect(HandlerMetricaDominio.handle_valores_acualizados, signal=f'{PromediosValoresActualizados.__name__}Dominio')