from uuid import UUID
from src.pda.config.session import Session
from src.pda.modulos.transacciones.dominio.entidades import Transaccion
from src.pda.modulos.transacciones.dominio.fabricas import FabricaTransacciones
from src.pda.modulos.transacciones.dominio.repositorios import RepositorioTransacciones
from src.pda.modulos.transacciones.infraestructura.dto import Transaccion as TransaccionDTO
from src.pda.modulos.transacciones.infraestructura.mapeadores import MapeadorTransaccion

class RepositorioTransaccionesSQLite(RepositorioTransacciones):
    def __init__(self):
        self.fabrica_transacciones: FabricaTransacciones = FabricaTransacciones()

    def obtener_por_id(self, id: UUID) -> Transaccion:
        session = Session()
        transaccion_dto = session.query(TransaccionDTO).filter(TransaccionDTO.id==str(id)).first()
        session.close()
        return self.fabrica_transacciones.crear_objeto(transaccion_dto, MapeadorTransaccion())

    def obtener_todos(self) -> list[Transaccion]:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Transaccion):
        transaccion_dto = self.fabrica_transacciones.crear_objeto(entity, MapeadorTransaccion())
        session = Session()
        session.add(transaccion_dto)
        session.commit()

    def actualizar(self, entity: Transaccion):
        ...

    def eliminar(self, entity_id: UUID):
        ...
