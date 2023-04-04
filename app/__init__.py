import os
import platform

from flask import Flask

from app.api import register_blueprints_v1


def register_blueprints(app):
    register_blueprints_v1(app)


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config/config.py')

    system = platform.system()
    env = os.environ.get('FLASK_ENV')

    if env is None:
        if system == 'Windows':
            env = 'development'
        else:
            env = 'production'

    if env == 'development':
        app.config.from_pyfile('config/config_dev.py')
    elif env == 'production':
        app.config.from_pyfile('config/config_prod.py')

    register_blueprints(app)
    return app
