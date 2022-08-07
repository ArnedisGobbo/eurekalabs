from flask import Flask
from flask_restful import Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from application.logger import setup_log
from resources.stock import Stock
from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'

limiter = Limiter(app, key_func=get_remote_address, default_limits=["10 per minute"])

api = Api(app)

setup_log('DEBUG')

api.add_resource(UserRegister, '/register')
api.add_resource(Stock, '/stock')

if __name__ == '__main__':
    from db.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
