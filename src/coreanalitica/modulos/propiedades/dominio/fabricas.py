from dataclasses import dataclass
from src.coreanalitica.modulos.propiedades.dominio.entidades import Metricas
from src.coreanalitica.modulos.propiedades.dominio.reglas import ValorNoNegativo
from src.coreanalitica.seedwork.dominio.entidades import Entidad
from src.coreanalitica.seedwork.dominio.fabricas import Fabrica
from src.coreanalitica.seedwork.dominio.repositorios import Mapeador


@dataclass
class FabricaMetricas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador=None) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Metricas = mapeador.dto_a_entidad(obj)

            self.validar_regla(ValorNoNegativo(propiedad.valor))

            return propiedad
