from flask import Blueprint

api = Blueprint('api', __name__)


@api.get('/ping')
def ping():
    return {'message': 'pong'}
