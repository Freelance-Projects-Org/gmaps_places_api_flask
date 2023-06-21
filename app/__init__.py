from flask import Flask
from app.apis.components import init_components

def create_app(env:str):
    app = Flask(__name__)          
    init_components(application=app,environment=env)
    # register blueprints of applications
    from app.apis.main import main as main_bp
    app.register_blueprint(main_bp)

    return app