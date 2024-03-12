from uuid import UUID
from src.auditoria.config.db import db
from src.auditoria.modulos.propiedades.dominio.entidades import Propiedad
from src.auditoria.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from src.auditoria.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from src.auditoria.modulos.propiedades.infraestructura.dto import Propiedad as PropiedadDTO
from src.auditoria.modulos.propiedades.infraestructura.mapeadores import MapeadorPropiedad
from src.auditoria.seedwork.dominio.excepciones import ExcepcionNoEncontrado
import random


class RepositorioPropiedadesPostgreSQL(RepositorioPropiedades):
    def __init__(self):
        self.fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter(PropiedadDTO.id==str(id)).one_or_none()
        if not propiedad_dto:
            raise ExcepcionNoEncontrado()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Propiedad):
        propiedad_dto = self.fabrica_propiedades.crear_objeto(entity, MapeadorPropiedad())
        db.session.add(propiedad_dto)
        db.session.commit()

    def actualizar(self, id: UUID, indice_confiabilidad: float):
        try:
            propiedad_dto = db.session.query(PropiedadDTO).filter(PropiedadDTO.id==str(id)).one_or_none()
            if not propiedad_dto:
                raise ExcepcionNoEncontrado()
            propiedad_dto.indice_confiabilidad = indice_confiabilidad
            #Valida las reglas de negocio nuevamente
            propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
            db.session.commit()
            return propiedad, 1
        except:
            propiedad = Propiedad(id=id, indice_confiabilidad=indice_confiabilidad)
            return propiedad, 0
    
    def actualizar_propiedad(self, dto):
        propiedad_dto = db.session.query(PropiedadDTO).filter(PropiedadDTO.id==str(dto.id_propiedad)).one_or_none()
        if not propiedad_dto:
            raise ExcepcionNoEncontrado()
        if dto.tipo_contrato == 1:
            propiedad_dto.valor_compra = dto.valor
            propiedad_dto.fecha_ultima_compra = dto.fecha_inicio
        elif dto.tipo_contrato == 2:
            propiedad_dto.valor_arrendamiento = dto.valor
            propiedad_dto.fecha_ultimo_arrendamiento = dto.fecha_inicio
        propiedad_dto.indice_confiabilidad = float(random.randint(5, 10)) / 10
        #Valida las reglas de negocio nuevamente
        propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        db.session.commit()
        return propiedad

    def eliminar(self, entity_id: UUID):
        ...
