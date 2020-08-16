from flask import Blueprint
from flask_restx import Api

from .user import api as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/1')

api = Api(
    blueprint,
    title='This is my comic app',
    version='1.0',
    description='This is the comic server application for architectural flask implementation ',
    # All API metadatas
)

api.add_namespace(ns1)