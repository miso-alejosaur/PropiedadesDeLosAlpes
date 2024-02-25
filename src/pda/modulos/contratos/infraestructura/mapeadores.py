from datetime import datetime
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.objetos_valor import Divisa, Fechas, Valor, TipoContrato, Pais
from src.pda.modulos.contratos.infraestructura.dto import Contrato as ContratoDTO
from src.pda.seedwork.dominio.repositorios import Mapeador

class MapeadorContrato(Mapeador):
    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        transaccion_dto = ContratoDTO()
        transaccion_dto.id = str(entidad.id)
        transaccion_dto.valor = entidad.valor.monto
        transaccion_dto.fecha_inicio = datetime(entidad.fechas.fecha_inicio.year, entidad.fechas.fecha_inicio.month, entidad.fechas.fecha_inicio.day)
        transaccion_dto.fecha_vencimiento = datetime(entidad.fechas.fecha_vencimiento.year, entidad.fechas.fecha_vencimiento.month, entidad.fechas.fecha_vencimiento.day)
        transaccion_dto.divisa = entidad.divisa.codigo
        transaccion_dto.pais = entidad.pais.nombre
        transaccion_dto.tipo_contrato = entidad.tipo_contrato.tipo_contrato

        return transaccion_dto

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        transaccion = Contrato(dto.id)
        transaccion.divisa = Divisa(dto.divisa)
        transaccion.fechas = Fechas(dto.fecha_inicio, dto.fecha_vencimiento)
        transaccion.valor = Valor(dto.valor)
        transaccion.pais = Pais(dto.pais)
        transaccion.tipo_contrato = TipoContrato(dto.tipo_contrato)

        return transaccion
