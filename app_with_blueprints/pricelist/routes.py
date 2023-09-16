from flask import Blueprint

pricelist = Blueprint(
    'pricelist_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@pricelist.route('/')
def index():
    return '<h1>Welcome to the home page!</h1>'
