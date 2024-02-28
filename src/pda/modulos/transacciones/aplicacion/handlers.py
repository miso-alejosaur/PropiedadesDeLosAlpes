from src.pda.modulos.transacciones.dominio.eventos import TransaccionCreada
from src.pda.seedwork.aplicacion.handlers import Handler
from src.pda.modulos.transacciones.infraestructura.despachadores import Despachador

class HandlerTransaccionIntegracion(Handler):

    @staticmethod
    def handle_transaccion_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-transaccion')
    