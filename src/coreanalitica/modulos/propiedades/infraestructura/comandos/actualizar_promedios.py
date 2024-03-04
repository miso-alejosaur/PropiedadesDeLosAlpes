from src.auditoria.seedwork.infraestructura.comandos import Comando
from .base import PropiedadBaseHandler
from dataclasses import dataclass, field
from src.coreanalitica.seedwork.infraestructura.comandos import ejecutar_commando as comando
from src.coreanalitica.modulos.propiedades.infraestructura.repositorios import RepositorioMetricas
from src.coreanalitica.modulos.propiedades.dominio.entidades import Metricas
from src.coreanalitica.seedwork.dominio.eventos import EventoDominio, EventoIntegracion
from pydispatch import dispatcher

@dataclass
class ActualizarPromedios(Comando):
    pais: str
    valor_arrendamiento: float
    valor_compra: float


class ActualizarPromediosHandler(PropiedadBaseHandler):
    
    def handle(self, comando: ActualizarPromedios):

        try:
            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioMetricas.__class__)
            metrica: Metricas = repositorio.actualizar(comando.pais,comando.valor_arrendamiento, comando.valor_compra)
            metrica.actualizar_valores(metrica)
            for evento in metrica.eventos:
                if isinstance(evento, EventoDominio):
                    print(evento, f'{type(evento).__name__}Dominio')
                    dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
        except Exception as e:
            print("Actualizacion no exitosa: " + str(e))


@comando.register(ActualizarPromedios)
def ejecutar_comando_actualizar_abono_contrato(comando: ActualizarPromedios):
    handler = ActualizarPromediosHandler()
    handler.handle(comando)
    