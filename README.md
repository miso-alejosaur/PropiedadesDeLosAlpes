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
