import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session


basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import src.pda.modulos.contratos.aplicacion
    import src.pda.modulos.transacciones.aplicacion

def importar_modelos_alchemy():
    import src.pda.modulos.contratos.infraestructura.dto
    import src.pda.modulos.transacciones.infraestructura.dto

def comenzar_consumidor(app):
    import threading
    import src.pda.modulos.transacciones.infraestructura.consumidores as transacciones
    import src.pda.modulos.contratos.infraestructura.consumidores as contratos

    # Suscripción a eventos
    threading.Thread(target=transacciones.suscribirse_a_eventos).start()
    threading.Thread(target=contratos.suscribirse_a_eventos).start()

    # Suscripción a comandos
    threading.Thread(target=transacciones.suscribirse_a_comandos, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_a_comandos, args=[app]).start()


def create_app():
    
    app = Flask(__name__, instance_relative_config=True)
    from src.pda.config.engine import url_postgresql_for_create_engine
    app.config['SQLALCHEMY_DATABASE_URI'] = url_postgresql_for_create_engine(
        username=os.getenv("DB_USER"),
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'

    from src.pda.config.db import init_db
    init_db(app)

    importar_modelos_alchemy()
    registrar_handlers()

    from src.pda.config.db import db

    with app.app_context():
        db.create_all()
        print(db)
        comenzar_consumidor(app)

    from src.pda.api import transacciones
    from src.pda.api import contratos
    app.register_blueprint(transacciones.bp)
    app.register_blueprint(contratos.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    @app.route("/ping")
    def health():
        return "pong"
    app.run(debug=True, port=80, host='0.0.0.0')