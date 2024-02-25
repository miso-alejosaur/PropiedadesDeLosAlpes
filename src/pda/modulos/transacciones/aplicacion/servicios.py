
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
    def _fabrica_transacciones(self):
        return self._fabrica_transacciones
