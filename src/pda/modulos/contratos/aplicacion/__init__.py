from pydispatch import dispatcher

from .handlers import HandlerContratoIntegracion

from src.pda.modulos.contratos.dominio.eventos import AbonoContratoActualizado

dispatcher.connect(HandlerContratoIntegracion.handle_abono_contrato_actualizado, signal=f'{AbonoContratoActualizado.__name__}Dominio')