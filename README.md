**Estructura:**
Este repositorio contiene el B/E de Propiedades de los Alpes. Dentro de la carpeta PDA se encuentra el código de esta manera:
- API: Contiene las rutas de entrada a los endpoints de los dos módulos desarrollados.
- config: Contiene la configuración de la base de datos PostgreSQL.
- modulos: Contiene todo el código del servicio desarrollado. Cada módulo (contratos y transacciones) está dividido en capa de aplicación, dominio e infraestructura, siguiendo los patrones de DDD vistos en el curso.
- seedwork: Contiene el código base sobre el cual se construyeron las clases de los módulos desarrollados.

**Despliegue:**
Para desplegar el proyecto es necesario primero crear un archivo .env en la raíz del proyecto y copiar la información que se encuentra en el archivo .env.template.
Posteriormente, solo es necesario ejecutar los comandos:
- docker-compose build
- docker-compose up

**Probar endpoints:**
- Crear contrato: http://localhost:6150/contratos/contrato-query/<id-contrato>

- Crear transaccion: http://localhost:6150/transacciones/transaccion
Body: {
  "fecha": "2020-03-02T12:12:00Z",
  "valor": 3393.2,
  "divisa": "COP",
  "id_contrato": "283a8154-808c-4c12-b406-fb4b1b79eb41"

}

**Justificación uso sistema de versionamiento y evolución de esquemas:**
Para nuestro proyecto decidimos usar Avro, la principal razón fue que teniamos ya ejemplos para implementar asi que esto agilizaba la curva de aprendizaje, además de dar guia y soporte durante del desarrollo a demás de facilitarse el entiendimiento de los mensajes al soportar JSON.

**Justificación CRUD o EventSourcing:**
La decicion que tomamos fue hacer uso de CRUD esta decision estuvo dada por varios puntos importantes, uno de ellos es que el EventSourcing es más robusto en cuanto almacenamiento de información, cosa que no necesitabamos pues no requeriamos almacenar eventos que nos mostraran la evolucion o cambio de datos. Además de complejizar un poco la arquitectura, y consideramos que no tendria mucho sentido ya que las operaciones que realizamos son básicas y sería una mala práctica complejizar sin ser necesario.

**Justificación uso de topologia de administración de datos- hibrido:**
El flujo comienza cuando se crea un contrato en el modulo de contratos el cual hace parte de un microservicio con su propia BD,en nuestro caso al analizar el negocio, entre los microservicios auditoria y core analitica decidimos utilizar un modelo hibrido dado que cuando se reciben los eventos de auditoria de la celebración de un contrato, core analitica va a generar metricas sobre esos mismos registros solo aumentando el promedio de valor de contratos por pais, es una metrica relativamente pequeña asi que no requiere una BD separada de esta manera se ahorraran costos de infraestructura al hacer un despliegue de la aplicación en la nube y disponibilizarlo allí, por esto core analitica y auditoria comparten BD.

**Escenarios a probar para la siguiente entrega:**
1. Escenario #3: Enriquecimiento de datos sin degradación de del servicio
2. Escenario #6: Modificar un componente de infraestructura no requiere cambios en la logica del dominio.
3. Escenario #8: Traducción a formato estandarizado para información de distintas fuentes.


| Integrante | Actividades |

| Carlos Torres | Microservicio de Auditoria, configuracion pulsar, pruebas de funcionamiento |
| Brahian Munar | Microservicio de Auditoria, configuracion pulsar |
| Alejando Santamaria | Microservicio de Auditoria, configuracion docker compose, pruebas de funcionamiento |
| Romy Caicedo | Microservicio de Auditoria, configuracion docker compose, ReadMe |

