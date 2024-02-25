from dataclasses import dataclass
from src.pda.modulos.contratos.dominio.repositorios import RepositorioContratos
from src.pda.modulos.contratos.infraestructura.repositorios import RepositorioContratosPostgreSQL

from src.pda.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio():
    def crear_objeto(self, obj: type) -> Repositorio:
        if obj == RepositorioContratos.__class__:
            return RepositorioContratosPostgreSQL()

        raise Exception()
