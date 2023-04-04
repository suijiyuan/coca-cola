from flask import Flask

from app.api import register_blueprints_v1


def register_blueprints(app):
    register_blueprints_v1(app)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    return app
