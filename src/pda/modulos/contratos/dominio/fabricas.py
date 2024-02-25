from attr import dataclass
from pda.modulos.contratos.dominio.entidades import Contrato
from pda.modulos.contratos.dominio.reglas import ValorNoNegativo, VencimientoValido, FechasValidas
from pda.seedwork.dominio.entidades import Entidad
from pda.seedwork.dominio.fabricas import Fabrica
from pda.seedwork.dominio.repositorios import Mapeador


@dataclass
class FabricaContratos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador=None) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            contrato: Contrato = mapeador.dto_a_entidad(obj)

            self.validar_regla(ValorNoNegativo(contrato))
            self.validar_regla(VencimientoValido(contrato))
            self.validar_regla(FechasValidas(contrato))

            return contrato
