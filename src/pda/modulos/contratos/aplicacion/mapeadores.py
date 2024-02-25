from datetime import date, time, datetime
from src.pda.modulos.contratos.aplicacion.dto import ContratoDTO
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.objetos_valor import Divisa, Fechas, Valor, TipoContrato, Pais
from src.pda.seedwork.dominio.repositorios import Mapeador as RepMap
from src.pda.seedwork.aplicacion.dto import Mapeador as AppMap

class MapeadorContrato(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Contrato.__class__


    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:

        return ContratoDTO(entidad.valor.monto,
                           entidad.fechas.fecha_inicio.strftime(self._FORMATO_FECHA),
                           entidad.fechas.fecha_vencimiento.strftime(self._FORMATO_FECHA),
                           entidad.tipo_contrato.tipo_contrato,
                           entidad.pais.nombre,
                           entidad.divisa.codigo,
                           entidad.valor.abono)

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:

        fecha_string_inicio = datetime.strptime(dto.fecha_inicio, self._FORMATO_FECHA)
        fecha_string_vencimiento = datetime.strptime(dto.fecha_vencimiento, self._FORMATO_FECHA)

        contrato = Contrato(valor=Valor(dto.valor, dto.valor_abonado),
                            fechas=Fechas(fecha_inicio=fecha_string_inicio.date(),
                                          fecha_vencimiento=fecha_string_vencimiento.date()),
                            tipo_contrato = TipoContrato(dto.tipo_contrato),
                            pais = Pais(dto.pais),
                            divisa=Divisa(dto.divisa))

        return contrato

class MapContratoDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ContratoDTO:
        contrato_dto = ContratoDTO(externo["valor"], externo["fechas"], externo["tipo_contrato"], externo["pais"], externo["divisa"])

        return contrato_dto

    def dto_a_externo(self, dto: ContratoDTO) -> dict:
        return dto.__dict__
