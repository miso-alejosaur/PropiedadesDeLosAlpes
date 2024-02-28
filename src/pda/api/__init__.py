from flask import Flask
from src.pda.api import transacciones
from src.pda.api import contratos

def registrar_handlers():
    #import src.pda.modulos.contratos.aplicacion
    import src.pda.modulos.transacciones.aplicacion

def create_app():
    
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.register_blueprint(transacciones.bp)
    app.register_blueprint(contratos.bp)
    return app

if __name__ == "__main__":
    app = create_app()
    @app.route("/ping")
    def health():
        return "pong"
    app.run(debug=True, port=80, host='0.0.0.0')