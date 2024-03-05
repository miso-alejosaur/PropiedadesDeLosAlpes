from src.pda.modulos.contratos.dominio.eventos import AbonoContratoActualizado, ContratoCreado
from src.pda.seedwork.aplicacion.handlers import Handler
from src.pda.modulos.contratos.infraestructura.despachadores import Despachador

class HandlerContratoDominio(Handler):

    @staticmethod
    def handle_abono_contrato_actualizado(evento):
        print(f'Evento recibido: {evento}')

class HandlerContratoIntegracion(Handler):

    @staticmethod
    def handle_contrato_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-contratos-auditoria')