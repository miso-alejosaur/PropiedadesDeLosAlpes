from src.coreanalitica.modulos.propiedades.dominio.eventos import PromediosValoresActualizados
from src.coreanalitica.seedwork.aplicacion.handlers import Handler
from src.coreanalitica.modulos.propiedades.infraestructura.despachadores import Despachador
    
class HandlerMetricaDominio(Handler):

    @staticmethod
    def handle_valores_acualizados(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-core')