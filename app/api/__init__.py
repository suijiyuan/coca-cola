from flask import Blueprint

from app.api.v1 import check


def create_blueprint_v1():
    blueprint_v1 = Blueprint('blueprint_v1', __name__)
    check.api.register(blueprint_v1, url_prefix='/check')
    return blueprint_v1
