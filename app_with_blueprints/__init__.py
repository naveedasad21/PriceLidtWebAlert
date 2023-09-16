from flask import Flask
from .pricelist.routes import pricelist


def create_app():

    app = Flask(__name__)
    app.register_blueprint(pricelist, url_prefix='/pricelis_home')
    return app
