from dataclasses import dataclass
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.reglas import ValorNoNegativo, VencimientoValido, FechasValidas
from src.pda.seedwork.dominio.entidades import Entidad
from src.pda.seedwork.dominio.fabricas import Fabrica
from src.pda.seedwork.dominio.repositorios import Mapeador


@dataclass
class FabricaContratos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador=None) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            contrato: Contrato = mapeador.dto_a_entidad(obj)

            self.validar_regla(ValorNoNegativo(contrato.valor))
            self.validar_regla(VencimientoValido(contrato.fechas, contrato.tipo_contrato))
            self.validar_regla(FechasValidas(contrato.fechas))

            return contrato
