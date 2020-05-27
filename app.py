from flask import Flask
from flask_restful import Api
from resources.grocery import Grocery, GroceryList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


db.init_app(app)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Grocery, '/grocery')
api.add_resource(GroceryList, '/groceries')

if __name__ == '__main__':
    app.run()
