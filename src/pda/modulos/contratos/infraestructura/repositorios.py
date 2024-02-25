from uuid import UUID
from pda.config.db import db
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.fabricas import FabricaContratos
from src.pda.modulos.contratos.dominio.repositorios import RepositorioContratos
from src.pda.modulos.contratos.infraestructura.dto import Contrato as ContratoDTO
from src.pda.modulos.contratos.infraestructura.mapeadores import MapeadorContrato

class RepositorioContratosPostgreSQL(RepositorioContratos):
    def __init__(self):
        self.fabrica_contratos: FabricaContratos = FabricaContratos()

    def obtener_por_id(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter_by(id=str(id)).one()
        return self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())

    def obtener_todos(self) -> list[Contrato]:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Contrato):
        contrato_dto = self.fabrica_contratos.crear_objeto(entity, MapeadorContrato())
        db.session.add(contrato_dto)
        db.session.commit()

    def actualizar(self, entity: Contrato):
        ...

    def eliminar(self, entity_id: UUID):
        ...
