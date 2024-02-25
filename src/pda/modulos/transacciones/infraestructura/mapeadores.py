from datetime import datetime
from pda.modulos.transacciones.dominio.entidades import Transaccion
from pda.modulos.transacciones.dominio.objetos_valor import Divisa, Fecha, Valor
from pda.modulos.transacciones.infraestructura.dto import Transaccion as TransaccionDTO
from pda.seedwork.dominio.repositorios import Mapeador

class MapeadorTransaccion(Mapeador):
    def obtener_tipo(self) -> type:
        return Transaccion.__class__

    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:
        print("transaccion", entidad)
        transaccion_dto = TransaccionDTO()
        transaccion_dto.id = str(entidad.id)
        transaccion_dto.valor = entidad.valor.monto
        print(entidad.fecha.fecha)
        transaccion_dto.fecha = datetime(entidad.fecha.fecha.year, entidad.fecha.fecha.month, entidad.fecha.fecha.day, entidad.fecha.hora.hour, entidad.fecha.hora.minute)
        transaccion_dto.divisa_id = entidad.divisa.codigo

        return transaccion_dto

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:
        transaccion = Transaccion(dto.id)
        transaccion.divisa = Divisa(dto.divisa.codigo, dto.divisa.nombre, dto.divisa.pais)
        transaccion.fecha = Fecha(dto.fecha.date, dto.fecha.time)
        transaccion.valor = Valor(dto.valor)

        return transaccion
