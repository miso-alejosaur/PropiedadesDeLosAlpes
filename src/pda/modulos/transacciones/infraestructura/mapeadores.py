from datetime import datetime
from src.pda.modulos.transacciones.dominio.entidades import Transaccion
from src.pda.modulos.transacciones.dominio.objetos_valor import Divisa, Fecha, Valor, Contrato
from src.pda.modulos.transacciones.infraestructura.dto import Transaccion as TransaccionDTO
from src.pda.seedwork.dominio.repositorios import Mapeador

class MapeadorTransaccion(Mapeador):
    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        transaccion_dto = TransaccionDTO()
        transaccion_dto.id = str(entidad.id)
        transaccion_dto.valor = entidad.valor.monto
        transaccion_dto.fecha = entidad.fecha.fecha.strftime('%Y-%m-%d')
        transaccion_dto.id_contrato = entidad.contrato.id_contrato
        transaccion_dto.divisa_id = entidad.divisa.codigo

        return transaccion_dto

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion(dto.id)
        transaccion.divisa = Divisa(dto.divisa.codigo, dto.divisa.nombre, dto.divisa.pais)
        transaccion.fecha = Fecha(dto.fecha.date, dto.fecha.time)
        transaccion.valor = Valor(dto.valor)
        transaccion.contrato = Contrato(dto.id_contrato)

        return transaccion
