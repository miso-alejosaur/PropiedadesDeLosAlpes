from src.auditoria.modulos.propiedades.dominio.objetos_valor import Valor, IndiceConfiabilidad
from src.auditoria.seedwork.dominio.reglas import ReglaNegocio

class ValorNoNegativo(ReglaNegocio):

    valor: Valor

    def __init__(self, valor, mensaje='El valor no debe tener montos negativos'):
        super().__init__(mensaje)
        self.valor = valor

    def es_valido(self) -> bool:
        return self.valor.valor_arrendamiento >= 0 and self.valor.valor_compra >= 0

class IndiceConfiabilidadValido(ReglaNegocio):

    indice_confiabilidad: IndiceConfiabilidad

    def __init__(self, indice_confiabilidad, mensaje='El indice de confiabilidad debe ser un valor entre 0 y 1'):
        super().__init__(mensaje)
        self.indice_confiabilidad = indice_confiabilidad

    def es_valido(self) -> bool:
        return self.indice_confiabilidad.indice >= 0 and self.indice_confiabilidad.indice <= 1