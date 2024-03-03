from src.pda.seedwork.aplicacion.comandos import ComandoHandler
from src.pda.modulos.transacciones.infraestructura.fabricas import FabricaRepositorio
from src.pda.modulos.transacciones.dominio.fabricas import FabricaTransacciones

class CrearTransaccionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_transacciones: FabricaTransacciones = FabricaTransacciones()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_transacciones(self):
        return self._fabrica_transacciones    
    