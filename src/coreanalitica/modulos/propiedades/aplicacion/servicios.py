
from datetime import date, time
import uuid
from src.coreanalitica.modulos.propiedades.dominio.entidades import Metricas
from src.coreanalitica.modulos.propiedades.dominio.fabricas import FabricaMetricas
from src.coreanalitica.modulos.propiedades.dominio.repositorios import RepositorioMetricas
from src.coreanalitica.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from src.coreanalitica.seedwork.aplicacion.servicios import Servicio


class ServicioContrato(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_metricas: FabricaMetricas = FabricaMetricas()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_metricas(self):
        return self._fabrica_metricas

