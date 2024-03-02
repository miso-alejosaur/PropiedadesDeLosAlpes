from src.pda.modulos.contratos.dominio.eventos import AbonoContratoActualizado
from src.pda.seedwork.aplicacion.handlers import Handler
from src.pda.modulos.contratos.infraestructura.despachadores import Despachador

class HandlerContratoIntegracion(Handler):

    @staticmethod
    def handle_abono_contrato_actualizado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-contrato')
    