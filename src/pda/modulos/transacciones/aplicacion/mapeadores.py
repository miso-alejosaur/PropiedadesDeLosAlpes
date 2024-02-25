from datetime import date, time, datetime
from src.pda.modulos.transacciones.aplicacion.dto import TransaccionDTO
from src.pda.modulos.transacciones.dominio.entidades import Transaccion
from src.pda.modulos.transacciones.dominio.objetos_valor import Divisa, Fecha, Valor,Contrato
from src.pda.seedwork.dominio.repositorios import Mapeador as RepMap
from src.pda.seedwork.aplicacion.dto import Mapeador as AppMap

class MapeadorTransaccion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Transaccion.__class__


    def entidad_a_dto(self, entidad: Transaccion) -> TransaccionDTO:

        combined_datetime = datetime.combine(entidad.fecha.fecha, entidad.fecha.hora)
        return TransaccionDTO(entidad.valor.monto, combined_datetime.strftime(self._FORMATO_FECHA), entidad.divisa.codigo, entidad.contrato)

    def dto_a_entidad(self, dto: TransaccionDTO) -> Transaccion:

        fecha_string = datetime.strptime(dto.fecha, self._FORMATO_FECHA)

        transaccion = Transaccion(valor=Valor(dto.valor), 
                                  fecha=Fecha(fecha=fecha_string.date(),
                                              hora=fecha_string.time()),
                                  divisa=Divisa("COP", "peso", "col"),
                                  contrato=Contrato(id_contrato=dto.contrato))

        return transaccion

class MapTransaccionDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> TransaccionDTO:
        transaccion_dto = TransaccionDTO(externo["valor"], externo["fecha"], externo["divisa"], externo["id_contrato"])

        return transaccion_dto

    def dto_a_externo(self, dto: TransaccionDTO) -> dict:
        return dto.__dict__
