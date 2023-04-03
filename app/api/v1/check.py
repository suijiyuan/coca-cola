from flask import Blueprint

from app.libs.my_print import MyPrint

api = MyPrint('check')


@api.route('/ping')
def ping():
    return 'pong'
