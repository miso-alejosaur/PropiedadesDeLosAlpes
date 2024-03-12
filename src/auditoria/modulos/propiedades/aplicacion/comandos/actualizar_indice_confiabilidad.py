from src.auditoria.seedwork.infraestructura.comandos import Comando
from .base import PropiedadBaseHandler
from dataclasses import dataclass, field
from src.auditoria.seedwork.infraestructura.comandos import ejecutar_commando as comando
from src.auditoria.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from src.auditoria.modulos.propiedades.dominio.entidades import Propiedad
from src.auditoria.seedwork.dominio.eventos import EventoDominio, EventoIntegracion
from pydispatch import dispatcher

@dataclass
class ActualizarIndiceConfiabilidad(Comando):
    id_propiedad: str
    indice_confiabilidad: float
    compensacion: bool
    
@dataclass
class RevertirIndiceConfiabilidad():
    id_propiedad: str
    indice_confiabilidad: float
    compensacion: bool

class ActualizarIndiceConfiabilidadHandler(PropiedadBaseHandler):
    
    def handle(self, comando: ActualizarIndiceConfiabilidad):

        try:
            repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
            propiedad: Propiedad = repositorio.actualizar(comando.id_propiedad, comando.indice_confiabilidad)
            propiedad.actualizar_indice_confiabilidad(propiedad)
            for evento in propiedad.eventos:
                if isinstance(evento, EventoDominio):
                    print(evento, f'{type(evento).__name__}Dominio')
                    dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
                elif isinstance(evento, EventoIntegracion):
                    print(evento, f'{type(evento).__name__}Integracion')
                    dispatcher.send(signal=f'{type(evento).__name__}Integracion', evento=evento)
        except Exception as e:
            print("Actualizacion no exitosa: " + str(e))


@comando.register(ActualizarIndiceConfiabilidad)
def ejecutar_comando_actualizar_abono_contrato(comando: ActualizarIndiceConfiabilidad):
    handler = ActualizarIndiceConfiabilidadHandler()
    handler.handle(comando)
    