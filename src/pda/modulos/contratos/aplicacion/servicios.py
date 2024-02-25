
from datetime import date, time
import uuid
from src.pda.modulos.contratos.dominio.entidades import Contrato
from src.pda.modulos.contratos.dominio.fabricas import FabricaContratos
from src.pda.modulos.contratos.dominio.repositorios import RepositorioContratos
from src.pda.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from src.pda.seedwork.aplicacion.servicios import Servicio


class ServicioContrato(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos

    def crear_contrato(self) -> Contrato:
        
        repo = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        return "ok"
