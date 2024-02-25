
from datetime import date, time
import uuid
from pda.modulos.contratos.dominio.entidades import Contrato
from pda.modulos.contratos.dominio.fabricas import FabricaContratos
from pda.modulos.contratos.dominio.objetos_valor import Divisa, Fechas, Valor
from pda.modulos.contratos.dominio.repositorios import RepositorioContratos
from pda.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from pda.seedwork.aplicacion.servicios import Servicio


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

    def crear_transaccion(self) -> Contrato:
        
        repo = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        return "ok"
