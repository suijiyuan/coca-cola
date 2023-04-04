from flask import Flask

from app.api import create_blueprint_v1


def register_blueprints(app):
    app.register_blueprint(create_blueprint_v1())


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    return app
