import os
from flask import Flask


# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import src.pda.modulos.transacciones.infraestructura.dto

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from src.pda.config.db import init_db
    init_db(app)

    from src.pda.config.db import db
    
    importar_modelos_alchemy()
    with app.app_context(): 
        db.create_all()

    from . import transacciones
    app.register_blueprint(transacciones.bp)

    @app.route("/ping")
    def health():
        return "pong"

    return app
