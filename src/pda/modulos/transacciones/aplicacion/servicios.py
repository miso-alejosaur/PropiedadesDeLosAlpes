
from datetime import date, time
from src.pda.modulos.transacciones.aplicacion.dto import TransaccionDTO
from src.pda.modulos.transacciones.aplicacion.mapeadores import MapeadorTransaccion
from src.pda.modulos.transacciones.dominio.entidades import Transaccion
from src.pda.modulos.transacciones.dominio.fabricas import FabricaTransacciones
from src.pda.modulos.transacciones.dominio.objetos_valor import Divisa, Fecha, Valor
from src.pda.modulos.transacciones.dominio.repositorios import RepositorioTransacciones
from src.pda.modulos.transacciones.infraestructura.fabricas import FabricaRepositorio
from src.pda.seedwork.aplicacion.servicios import Servicio
from src.tasks import app
from celery import Celery
from celery.contrib.methods import task_method

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

    @app.task(filter)
    def crear_transaccion(self, transaccion_dto: TransaccionDTO) -> Transaccion:
        
        repo = self.fabrica_repositorio.crear_objeto(RepositorioTransacciones.__class__)
        transaccion = self.fabrica_transacciones.crear_objeto(transaccion_dto, MapeadorTransaccion())
        
        repo.agregar(transaccion)

        return self.fabrica_transacciones.crear_objeto(transaccion, MapeadorTransaccion())
