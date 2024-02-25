from dataclasses import dataclass
from pda.modulos.transacciones.dominio.repositorios import RepositorioTransacciones
from pda.modulos.transacciones.infraestructura.repositorios import RepositorioTransaccionesSQLite

from pda.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio():
    def crear_objeto(self, obj: type) -> Repositorio:
        if obj == RepositorioTransacciones.__class__:
            return RepositorioTransaccionesSQLite()

        raise Exception()
