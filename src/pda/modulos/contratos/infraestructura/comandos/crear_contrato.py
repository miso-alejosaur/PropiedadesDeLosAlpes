from src.pda.seedwork.aplicacion.comandos import Comando
from src.pda.modulos.contratos.aplicacion.dto import ContratoDTO
from .base import ContratoBaseHandler
from dataclasses import dataclass, field
from src.pda.seedwork.infraestructura.comandos import ejecutar_commando as comando

from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from src.pda.modulos.contratos.infraestructura.repositorios import RepositorioContratos
from pydispatch import dispatcher

@dataclass
class CrearContrato(Comando):
    valor: float
    valor_abonado: float
    fecha_inicio: str
    fecha_vencimiento: str
    divisa: str
    pais: str
    tipo_contrato: int
    id_propiedad: str


class CrearContratoHandler(ContratoBaseHandler):
    
    def handle(self, comando: CrearContrato):
        contrato_dto = ContratoDTO(
                valor=comando.valor
            ,   valor_abonado=comando.valor_abonado 
            ,   fecha_inicio=comando.fecha_inicio
            ,   fecha_vencimiento=comando.fecha_vencimiento
            ,   pais=comando.pais
            ,   divisa=comando.divisa
            ,   tipo_contrato=comando.tipo_contrato
            ,   id_propiedad=comando.id_propiedad
            )
        contrato: Contrato = self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        contrato.crear_contrato(contrato)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        repositorio.agregar(contrato)
        for evento in contrato.eventos:
            print(evento, f'{type(evento).__name__}Integracion')
            dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)



@comando.register(CrearContrato)
def ejecutar_comando_crear_contrato(comando: CrearContrato):
    handler = CrearContratoHandler()
    handler.handle(comando)
    