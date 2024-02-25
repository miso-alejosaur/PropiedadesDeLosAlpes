from datetime import date, time, datetime
from pda.modulos.transacciones.aplicacion.dto import TransaccionDTO
from pda.modulos.transacciones.dominio.entidades import Transaccion
from pda.modulos.transacciones.dominio.objetos_valor import Divisa, Fecha, Valor
from pda.seedwork.dominio.repositorios import Mapeador as RepMap
from pda.seedwork.aplicacion.dto import Mapeador as AppMap

class MapeadorTransaccion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Transaccion.__class__


    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:

        combined_datetime = datetime.combine(entidad.fecha.fecha, entidad.fecha.hora)
        return TransaccionDTO(entidad.valor.monto, combined_datetime.strftime(self._FORMATO_FECHA), entidad.divisa.codigo)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:

        fecha_string = datetime.strptime(dto.fecha, self._FORMATO_FECHA)

        transaccion = Transaccion(valor=Valor(dto.valor), 
                                  fecha=Fecha(fecha=fecha_string.date(),
                                              hora=fecha_string.time()),
                                  divisa=Divisa("COP", "peso", "col"))

        return transaccion

class MapTransaccionDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> TransaccionDTO:
        transaccion_dto = TransaccionDTO(externo["valor"], externo["fecha"], externo["divisa"])

        return transaccion_dto

    def dto_a_externo(self, dto: TransaccionDTO) -> dict:
        return dto.__dict__
