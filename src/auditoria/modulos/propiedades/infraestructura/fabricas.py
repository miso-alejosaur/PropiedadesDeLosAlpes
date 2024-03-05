from dataclasses import dataclass
from src.auditoria.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from src.auditoria.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedadesPostgreSQL

from src.auditoria.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio():
    def crear_objeto(self, obj: type) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesPostgreSQL()

        raise Exception()
