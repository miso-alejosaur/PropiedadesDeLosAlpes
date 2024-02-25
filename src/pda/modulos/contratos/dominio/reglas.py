from pda.modulos.contratos.dominio.objetos_valor import Valor, Fechas, TipoContrato, TipoContratoEnum
from pda.seedwork.dominio.reglas import ReglaNegocio

class ValorNoNegativo(ReglaNegocio):

    valor: Valor

    def __init__(self, valor, mensaje='El valor debe ser no negativo'):
        super().__init__(mensaje)
        self.valor = valor

    def es_valido(self) -> bool:
        return self.valor.monto != self.valor.monto
    
class VencimientoValido(ReglaNegocio):

    fechas: Fechas
    tipo_contrato: TipoContrato

    def __init__(self, fechas, tipo_contrato, mensaje='Un contrato de arrendamiento debe tener una fecha de vencimiento'):
        super().__init__(mensaje)
        self.fechas = fechas
        self.tipo_contrato = tipo_contrato

    def es_valido(self) -> bool:
        if self.tipo_contrato.tipo_contrato == TipoContratoEnum.ARRENDAMIENTO:
            if not self.fechas.fecha_vencimiento:
                return False
        return True

class FechasValidas(ReglaNegocio):

    fechas: Fechas
    tipo_contrato: TipoContrato

    def __init__(self, fechas, mensaje='La fecha de vencimiento debe ser posterior a la de inicio'):
        super().__init__(mensaje)
        self.fechas = fechas

    def es_valido(self) -> bool:
        if self.fechas.fecha_vencimiento: 
            return self.fechas.fecha_inicio < self.fechas.fecha_vencimiento
        return True