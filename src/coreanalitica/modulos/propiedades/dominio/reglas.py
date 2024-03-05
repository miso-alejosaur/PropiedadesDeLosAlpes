from src.coreanalitica.modulos.propiedades.dominio.objetos_valor import Valor
from src.coreanalitica.seedwork.dominio.reglas import ReglaNegocio

class ValorNoNegativo(ReglaNegocio):

    valor: Valor

    def __init__(self, valor, mensaje='El valor no debe tener montos negativos'):
        super().__init__(mensaje)
        self.valor = valor

    def es_valido(self) -> bool:
        return self.valor.valor_arrendamiento >= 0 and self.valor.valor_compra >= 0
