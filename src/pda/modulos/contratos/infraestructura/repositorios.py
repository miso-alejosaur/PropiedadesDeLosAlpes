from uuid import UUID
from src.pda.config.session import Session
from src.pda.config.db import db
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.fabricas import FabricaContratos
from src.pda.modulos.contratos.dominio.repositorios import RepositorioContratos
from src.pda.modulos.contratos.infraestructura.dto import Contrato as ContratoDTO
from src.pda.modulos.contratos.infraestructura.mapeadores import MapeadorContrato
from src.pda.seedwork.dominio.excepciones import ExcepcionNoEncontrado

class RepositorioContratosPostgreSQL(RepositorioContratos):
    def __init__(self):
        self.fabrica_contratos: FabricaContratos = FabricaContratos()

    def obtener_por_id(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter(ContratoDTO.id==str(id)).one_or_none()
        if not contrato_dto:
            raise ExcepcionNoEncontrado()
        return self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())

    def obtener_todos(self) -> list[Contrato]:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Contrato):
        contrato_dto = self.fabrica_contratos.crear_objeto(entity, MapeadorContrato())
        db.session.add(contrato_dto)
        db.session.commit()

    def actualizar(self, id: UUID, abono: float):
        contrato_dto = db.session.query(ContratoDTO).filter(ContratoDTO.id==str(id)).one_or_none()
        contrato_dto.valor_abonado += abono
        #Valida las reglas de negocio nuevamente
        self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        db.session.commit()

    def eliminar(self, entity_id: UUID):
        ...
