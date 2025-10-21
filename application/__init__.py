from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import Home, User, Users, HealthCheck


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    init_db(app)

    api = Api(app)
    api.add_resource(Home, '/')
    api.add_resource(HealthCheck, '/health')
    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')

    return app
