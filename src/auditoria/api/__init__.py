import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session


basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import src.auditoria.modulos.propiedades.aplicacion

def importar_modelos_alchemy():
    import src.auditoria.modulos.propiedades.infraestructura.dto

def comenzar_consumidor(app):
    import threading
    import src.auditoria.modulos.propiedades.infraestructura.consumidores as propiedades

    # Suscripción a eventos
    threading.Thread(target=propiedades.suscribirse_a_eventos, args=[app]).start()

    # Suscripción a comandos
    threading.Thread(target=propiedades.suscribirse_a_comandos, args=[app]).start()


def create_app():
    
    app = Flask(__name__, instance_relative_config=True)
    from src.auditoria.config.engine import url_postgresql_for_create_engine
    app.config['SQLALCHEMY_DATABASE_URI'] = url_postgresql_for_create_engine(
        username=os.getenv("DB_USER_PROPIEDADES"),
        host=os.getenv("DB_HOST_PROPIEDADES"),
        database=os.getenv("DB_NAME_PROPIEDADES"),
        password=os.getenv("DB_PASSWORD_PROPIEDADES"),
        port=os.getenv("DB_PORT_PROPIEDADES"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e37c'
    app.config['SESSION_TYPE'] = 'filesystem'

    from src.auditoria.config.db import init_db
    init_db(app)

    importar_modelos_alchemy()
    registrar_handlers()

    from src.auditoria.config.db import db

    with app.app_context():
        db.create_all()
        comenzar_consumidor(app)

    from src.auditoria.api import auditoria
    app.register_blueprint(auditoria.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    @app.route("/ping")
    def health():
        return "pong"
    app.run(debug=True, port=80, host='0.0.0.0')