from dataclasses import dataclass
from src.auditoria.modulos.propiedades.dominio.entidades import Propiedad
from src.auditoria.modulos.propiedades.dominio.reglas import ValorNoNegativo, IndiceConfiabilidadValido
from src.auditoria.seedwork.dominio.entidades import Entidad
from src.auditoria.seedwork.dominio.fabricas import Fabrica
from src.auditoria.seedwork.dominio.repositorios import Mapeador


@dataclass
class FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador=None) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)

            self.validar_regla(ValorNoNegativo(propiedad.valor))
            self.validar_regla(IndiceConfiabilidadValido(propiedad.indice_confiabilidad))

            return propiedad
