from src.auditoria.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin, Paso
from src.auditoria.seedwork.aplicacion.comandos import Comando
from src.auditoria.seedwork.dominio.eventos import EventoDominio
from src.auditoria.seedwork.aplicacion.handlers import Handler

from src.auditoria.modulos.sagas.aplicacion.comandos.contratos import CrearContrato, EliminarContrato
from src.auditoria.modulos.sagas.aplicacion.comandos.metricas import ActualizarPromedios, RevertirPromedios
from src.auditoria.modulos.propiedades.aplicacion.comandos.actualizar_indice_confiabilidad import ActualizarIndiceConfiabilidad, RevertirIndiceConfiabilidad

from src.auditoria.modulos.sagas.dominio.eventos.propiedades import IndiceConfiabilidadActualizado, IndiceActualizacionFallida
from src.auditoria.modulos.sagas.dominio.eventos.contratos import ContratoCreado, CreacionContratoFallido
from src.auditoria.modulos.sagas.dominio.eventos.metricas import PromediosValoresActualizados, PromediosActualizacionFallida
import uuid
import random
from src.auditoria.modulos.sagas.infraestructura.despachadores import Despachador
from src.auditoria.modulos.sagas.infraestructura.schema.v1.comandos import ComandoActualizarIndiceConfiabilidad, ComandoActualizarValoresPayload

class CoordinadorPropiedades(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearContrato, evento=ContratoCreado, error=CreacionContratoFallido, compensacion=EliminarContrato),
            Transaccion(index=2, comando=ActualizarIndiceConfiabilidad, evento=IndiceConfiabilidadActualizado, error=IndiceActualizacionFallida, compensacion=RevertirIndiceConfiabilidad),
            Transaccion(index=3, comando=ActualizarPromedios, evento=PromediosValoresActualizados, error=PromediosActualizacionFallida, compensacion=RevertirPromedios),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        ...

    def enviar_comando(self, comando: Comando, tipo_comando: type):
        despachador = Despachador()
        if tipo_comando == ActualizarIndiceConfiabilidad:
            despachador.publicar_comando(comando=comando, topico='comandos-auditoria', tipo_comando=ComandoActualizarIndiceConfiabilidad)
        elif tipo_comando == ActualizarPromedios:
            despachador.publicar_comando(comando=comando, topico='comandos-metricas', tipo_comando=ComandoActualizarValoresPayload)
        elif tipo_comando == RevertirIndiceConfiabilidad:
            despachador.publicar_comando(comando=comando, topico='comandos-auditoria', tipo_comando=ComandoActualizarIndiceConfiabilidad)
        

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        if tipo_comando == ActualizarIndiceConfiabilidad:
            return ActualizarIndiceConfiabilidad(id_propiedad=evento.id_propiedad, indice_confiabilidad=float(random.randint(8, 10)) / 10, compensacion=False)
        elif tipo_comando == ActualizarPromedios:
            return ActualizarPromedios(pais=evento.pais, valor_arrendamiento=evento.valor_arrendamiento, valor_compra=evento.valor_compra, id_propiedad=evento.id_propiedad, indice_confiabilidad=evento.indice_confiabilidad)
        elif tipo_comando == RevertirIndiceConfiabilidad:
            return RevertirIndiceConfiabilidad(id_propiedad=evento.id_propiedad, indice_confiabilidad=evento.indice_confiabilidad, compensacion=True)
        


class HandlerSagasDominio(Handler):

    @staticmethod
    def oir_mensaje(mensaje):
        if isinstance(mensaje, EventoDominio):
            coordinador = CoordinadorPropiedades()
            coordinador.inicializar_pasos()
            coordinador.procesar_evento(mensaje)
        else:
            raise NotImplementedError("El mensaje no es evento de Dominio")