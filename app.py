from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)

    from resources.task_resource import HelloWorld

    api = Api(app)
    api.add_resource(HelloWorld, '/')

    return app
