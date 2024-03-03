from pydispatch import dispatcher

from .handlers import HandlerPropiedadIntegracion, HandlerPropiedadDominio

from src.auditoria.modulos.propiedades.dominio.eventos import PropiedadDisponible, IndiceConfiabilidadActualizado

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_disponible, signal=f'{PropiedadDisponible.__name__}Integracion')
dispatcher.connect(HandlerPropiedadDominio.handle_indice_confiabilidad_actualizado, signal=f'{IndiceConfiabilidadActualizado.__name__}Dominio')