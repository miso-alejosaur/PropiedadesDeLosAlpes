from src.auditoria.modulos.propiedades.dominio.eventos import PropiedadDisponible
from src.auditoria.seedwork.aplicacion.handlers import Handler
from src.auditoria.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_disponible(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria-integracion')
    
class HandlerPropiedadDominio(Handler):

    @staticmethod
    def handle_indice_confiabilidad_actualizado(evento):
        print(f'Evento recibido: {evento}')