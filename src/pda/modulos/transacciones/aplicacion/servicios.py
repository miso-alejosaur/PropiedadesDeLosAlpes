
from datetime import date, time
from pda.modulos.transacciones.aplicacion.dto import TransaccionDTO
from pda.modulos.transacciones.aplicacion.mapeadores import MapeadorTransaccion
from pda.modulos.transacciones.dominio.entidades import Transaccion
from pda.modulos.transacciones.dominio.fabricas import FabricaTransacciones
from pda.modulos.transacciones.dominio.objetos_valor import Divisa, Fecha, Valor
from pda.modulos.transacciones.dominio.repositorios import RepositorioTransacciones
from pda.modulos.transacciones.infraestructura.fabricas import FabricaRepositorio
from pda.seedwork.aplicacion.servicios import Servicio


class ServicioTransaccion(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transacciones: FabricaTransacciones = FabricaTransacciones()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_transacciones(self):
        return self._fabrica_transacciones

    def crear_transaccion(self, transaccion_dto: TransaccionDTO) -> Transaccion:
        
        repo = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        transaccion = self.fabrica_transacciones.crear_objeto(transaccion_dto, MapeadorTransaccion())
        
        repo.agregar(transaccion)

        return self.fabrica_transacciones.crear_objeto(transaccion, MapeadorTransaccion())
