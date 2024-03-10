import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e87c'
    app.config['SESSION_TYPE'] = 'filesystem'

    from src.traductor.api import traductor_json
    from src.traductor.api import traductor_xml
    app.register_blueprint(traductor_json.bp)
    app.register_blueprint(traductor_xml.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    @app.route("/ping")
    def health():
        return "pong"
    app.run(debug=True, port=80, host='0.0.0.0')