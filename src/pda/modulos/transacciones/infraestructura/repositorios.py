from uuid import UUID
from pda.modulos.transacciones.dominio.entidades import Transaccion
from pda.modulos.transacciones.dominio.repositorios import RepositorioTransacciones


class RepositorioTransaccionesSQLite(RepositorioTransacciones):
    def __init__(self):
        self.fabrica_transacciones: FabricaTransacciones = FabricaTransacciones()

    def obtener_por_id(self, id: UUID) -> Transaccion:
        transaccion_dto = db.session.query(TransaccionDTO).filter_by(id=str(id)).one()
        return self.fabrica_transacciones.crear_objeto(transaccion_dto, MapeadorTransaccion())

    def obtener_todos(self) -> list[Transaccion]:
        # TODO
        raise NotImplementedError

    def agregar(self, transaccion: Transaccion):
        transaccion_dto = self.fabrica_transacciones.crear_objeto(transaccion, MapeadorTransaccion())
        db.session.add(transaccion_dto)
        db.session.commit()

    def actualizar(self, transaccion: Transaccion):
        ...

    def eliminar(self, transaccion_id: UUID):
        ...