from pydispatch import dispatcher

from .handlers import HandlerContratoIntegracion, HandlerContratoDominio

from src.pda.modulos.contratos.dominio.eventos import AbonoContratoActualizado, ContratoCreado

dispatcher.connect(HandlerContratoIntegracion.handle_contrato_creado, signal=f'{ContratoCreado.__name__}Integracion')
dispatcher.connect(HandlerContratoDominio.handle_abono_contrato_actualizado, signal=f'{AbonoContratoActualizado.__name__}Dominio')