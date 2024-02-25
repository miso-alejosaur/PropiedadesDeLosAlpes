from uuid import UUID
from src.pda.config.session import Session
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.fabricas import FabricaContratos
from src.pda.modulos.contratos.dominio.repositorios import RepositorioContratos
from src.pda.modulos.contratos.infraestructura.dto import Contrato as ContratoDTO
from src.pda.modulos.contratos.infraestructura.mapeadores import MapeadorContrato

class RepositorioContratosPostgreSQL(RepositorioContratos):
    def __init__(self):
        self.fabrica_contratos: FabricaContratos = FabricaContratos()

    def obtener_por_id(self, id: UUID) -> Contrato:
        session = Session()
        contrato_dto = session.query(ContratoDTO).filter(ContratoDTO.id==str(id)).one()
        return self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())

    def obtener_todos(self) -> list[Contrato]:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Contrato):
        session = Session()
        contrato_dto = self.fabrica_contratos.crear_objeto(entity, MapeadorContrato())
        session.add(contrato_dto)
        session.commit()

    def actualizar(self, entity: Contrato):
        ...

    def eliminar(self, entity_id: UUID):
        ...
