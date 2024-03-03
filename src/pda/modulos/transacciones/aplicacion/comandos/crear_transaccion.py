from src.pda.seedwork.aplicacion.comandos import Comando
from src.pda.modulos.transacciones.aplicacion.dto import TransaccionDTO
from .base import CrearTransaccionBaseHandler
from dataclasses import dataclass, field
from src.pda.seedwork.aplicacion.comandos import ejecutar_commando as comando

from src.pda.modulos.transacciones.dominio.entidades import Transaccion
from src.pda.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from src.pda.modulos.transacciones.aplicacion.mapeadores import MapeadorTransaccion
from src.pda.modulos.transacciones.infraestructura.repositorios import RepositorioTransacciones
from pydispatch import dispatcher

@dataclass
class CrearTransaccion(Comando):
    valor: float
    fecha: str
    divisa: str
    contrato: str


class CrearTransaccionHandler(CrearTransaccionBaseHandler):
    
    def handle(self, comando: CrearTransaccion):
        transaccion_dto = TransaccionDTO(
                valor=comando.valor
            ,   fecha=comando.fecha
            ,   divisa=comando.divisa
            ,   contrato=comando.contrato)
        transaccion: Transaccion = self.fabrica_transacciones.crear_objeto(transaccion_dto, MapeadorTransaccion())
        transaccion.crear_transaccion(transaccion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)

        repositorio.agregar(transaccion)
        for evento in transaccion.eventos:
            print(evento, f'{type(evento).__name__}Dominio')
            dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, transaccion)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()


@comando.register(CrearTransaccion)
def ejecutar_comando_crear_transaccion(comando: CrearTransaccion):
    handler = CrearTransaccionHandler()
    handler.handle(comando)
    