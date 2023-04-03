from flask import Blueprint

from app.api.v1 import check


def create_blueprint_v1():
    blueprint_v1 = Blueprint('blueprint_v1', __name__, url_prefix='/v1')
    blueprint_v1.register_blueprint(check.api)
    return blueprint_v1
