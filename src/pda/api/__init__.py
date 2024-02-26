from flask import Flask
from src.pda.api import transacciones


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(transacciones.bp)
    return app

if __name__ == "__main__":
    app = create_app()
    @app.route("/ping")
    def health():
        return "pong"
    app.run(debug=True, port=80, host='0.0.0.0')