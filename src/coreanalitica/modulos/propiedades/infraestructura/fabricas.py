from dataclasses import dataclass
from src.coreanalitica.modulos.propiedades.dominio.repositorios import RepositorioMetricas
from src.coreanalitica.modulos.propiedades.infraestructura.repositorios import RepositorioMetricasPostgreSQL

from src.coreanalitica.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio():
    def crear_objeto(self, obj: type) -> Repositorio:
        if obj == RepositorioMetricas.__class__:
            return RepositorioMetricasPostgreSQL()

        raise Exception()
