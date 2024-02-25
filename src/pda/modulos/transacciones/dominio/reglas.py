from pda.modulos.transacciones.dominio.objetos_valor import Valor
from pda.seedwork.dominio.reglas import ReglaNegocio

class ValorNoNegativo(ReglaNegocio):

    valor: Valor

    def __init__(self, valor, mensaje='El valor debe ser no negativo'):
        super().__init__(mensaje)
        self.valor = valor

    def es_valido(self) -> bool:
        return self.valor.monto != self.valor.monto
