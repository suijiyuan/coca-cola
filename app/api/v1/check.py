from flask import Blueprint

api = Blueprint('check', __name__, url_prefix='/check')


@api.route('/ping')
def ping():
    return 'pong'
