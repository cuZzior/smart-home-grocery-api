from flask import request
from flask_restful import Resource
from models.grocery import GroceryModel


class Grocery(Resource):
    def get(self):
        data = request.get_json()
        grocery = GroceryModel.find_by_id(data['id'])
        if grocery:
            return grocery.json()
        return {'message': 'No such grocery in database'}, 404

    def post(self):
        data = request.get_json()
        grocery = GroceryModel(data['name'], data['exp_date'])
        grocery.save_to_db()

        return {'message': 'Grocery added to database.'}

    def delete(self):
        data = request.get_json()
        grocery = GroceryModel.find_by_id(data['id'])
        if grocery:
            grocery.delete_from_db()
            return {'message': 'Grocery removed from database.'}
        return {'message': 'No such grocery in database'}, 404

    def put(self):
        data = request.get_json()
        grocery = GroceryModel.find_by_id(data['id'])
        if not grocery:
            grocery = GroceryModel(data['name'], data['exp_date'])
        else:
            grocery.exp_date = data['exp_date']
        grocery.save_to_db()
        return grocery.json()


class GroceryList(Resource):
    def get(self):
        return {'groceries': [grocery.json() for grocery in GroceryModel.query.all()]}
