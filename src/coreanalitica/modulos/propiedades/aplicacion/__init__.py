from pydispatch import dispatcher

from .handlers import HandlerMetricaDominio

from src.coreanalitica.modulos.propiedades.dominio.eventos import PromediosValoresActualizados

dispatcher.connect(HandlerMetricaDominio.handle_valores_acualizados, signal=f'{PromediosValoresActualizados.__name__}Dominio')