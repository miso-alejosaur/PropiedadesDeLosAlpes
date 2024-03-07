from src.coreanalitica.seedwork.aplicacion.queries import QueryHandler
from src.coreanalitica.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from src.coreanalitica.modulos.propiedades.dominio.fabricas import FabricaMetricas
class ContratosQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_metricas: FabricaMetricas = FabricaMetricas()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_metricas(self):
        return self._fabrica_metricas