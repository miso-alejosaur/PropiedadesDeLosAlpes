
from datetime import date, time
import uuid
from src.auditoria.modulos.propiedades.dominio.entidades import Propiedad
from src.auditoria.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from src.auditoria.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from src.auditoria.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from src.auditoria.seedwork.aplicacion.servicios import Servicio


class ServicioContrato(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

