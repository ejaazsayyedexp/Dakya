import os
from flask import Flask
from .modules.request import reqs

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(reqs.bp)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app