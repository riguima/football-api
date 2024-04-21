from importlib import import_module

from flask import Flask

from football_api.config import config


def load_extensions(app):
    for extension in config['EXTENSIONS']:
        extension_module = import_module(extension)
        extension_module.init_app(app)


def create_app():
    app = Flask(__name__)
    load_extensions(app)
    return app
