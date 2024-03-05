from src.pda.seedwork.infraestructura.comandos import ComandoHandler
from src.pda.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from src.pda.modulos.contratos.dominio.fabricas import FabricaContratos

class ContratoBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos    
    