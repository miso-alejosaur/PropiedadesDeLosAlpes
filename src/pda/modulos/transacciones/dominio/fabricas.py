from attr import dataclass
from src.pda.modulos.transacciones.dominio.entidades import Transaccion
from src.pda.modulos.transacciones.dominio.reglas import ValorNoNegativo
from src.pda.seedwork.dominio.entidades import Entidad
from src.pda.seedwork.dominio.fabricas import Fabrica
from src.pda.seedwork.dominio.repositorios import Mapeador


@dataclass
class FabricaTransacciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador=None) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            transaccion: Transaccion = mapeador.dto_a_entidad(obj)

            self.validar_regla(ValorNoNegativo(transaccion.valor))

            return transaccion
