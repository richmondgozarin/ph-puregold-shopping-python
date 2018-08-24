from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

# local import
from app.apis.api import ShoppingApi, ShoppingListApi
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    api = Api(app)
    
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    # Actuall setup the Api resource routing here
    api.add_resource(ShoppingListApi, '/shoppings',  endpoint='shoppinglist')
    api.add_resource(ShoppingApi, '/shoppings/<shopping_id>',  endpoint='shopping')

    return app