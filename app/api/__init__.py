from flask import Blueprint

from app.api.v1 import check, create_blueprint_v1


def register_blueprints_v1(app):
    app.register_blueprint(create_blueprint_v1())
