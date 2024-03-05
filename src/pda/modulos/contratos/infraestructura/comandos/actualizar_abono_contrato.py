from src.pda.seedwork.aplicacion.comandos import Comando
from .base import ContratoBaseHandler
from dataclasses import dataclass, field
from src.pda.seedwork.infraestructura.comandos import ejecutar_commando as comando

from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.infraestructura.repositorios import RepositorioContratos
from pydispatch import dispatcher

@dataclass
class ActualizarAbonoContrato(Comando):
    valor_abonado: float
    id_contrato: str


class ActualizarAbonoContratoHandler(ContratoBaseHandler):
    
    def handle(self, comando: ActualizarAbonoContrato):

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)
        contrato: Contrato = repositorio.obtener_por_id(comando.id_contrato)
        contrato.actualizar_abono_contrato(contrato, comando.valor_abonado)

        repositorio.actualizar(comando.id_contrato, comando.valor_abonado)
        for evento in contrato.eventos:
            print(evento, f'{type(evento).__name__}Dominio')
            dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, transaccion)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()


@comando.register(ActualizarAbonoContrato)
def ejecutar_comando_actualizar_abono_contrato(comando: ActualizarAbonoContrato):
    handler = ActualizarAbonoContratoHandler()
    handler.handle(comando)
    