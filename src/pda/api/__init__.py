import os
from flask import Flask


# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from pda.config.db import init_db
    init_db(app)

    from pda.config.db import db
    with app.app_context(): 
        db.create_all()

    from . import transacciones
    app.register_blueprint(transacciones.bp)

    @app.route("/ping")
    def health():
        return "pong"

    return app
