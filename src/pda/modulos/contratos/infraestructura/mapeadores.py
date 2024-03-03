from datetime import datetime
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.objetos_valor import Divisa, Fechas, Valor, TipoContrato, Pais
from src.pda.modulos.contratos.infraestructura.dto import Contrato as ContratoDTO
from src.pda.seedwork.dominio.repositorios import Mapeador

class MapeadorContrato(Mapeador):
    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.id = str(entidad.id)
        contrato_dto.valor = entidad.valor.monto
        contrato_dto.fecha_inicio = datetime(entidad.fechas.fecha_inicio.year, entidad.fechas.fecha_inicio.month, entidad.fechas.fecha_inicio.day)
        contrato_dto.fecha_vencimiento = datetime(entidad.fechas.fecha_vencimiento.year, 
                                                  entidad.fechas.fecha_vencimiento.month, 
                                                  entidad.fechas.fecha_vencimiento.day) if entidad.fechas.fecha_vencimiento else None
        contrato_dto.divisa = entidad.divisa.codigo
        contrato_dto.pais = entidad.pais.nombre
        contrato_dto.tipo_contrato = entidad.tipo_contrato.tipo_contrato
        contrato_dto.valor_abonado = entidad.valor.abono

        return contrato_dto

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        contrato = Contrato(id=dto.id, 
                            valor=Valor(monto=dto.valor, abono=dto.valor_abonado), 
                            fechas=Fechas(fecha_inicio=dto.fecha_inicio, fecha_vencimiento=dto.fecha_vencimiento), 
                            tipo_contrato=TipoContrato(tipo_contrato=dto.tipo_contrato),
                            divisa=Divisa(codigo=dto.divisa),
                            pais=Pais(nombre=dto.pais))

        return contrato
