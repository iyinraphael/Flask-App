from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'item not found'}, 404

    def post(self, name):
        # checks if item exists
        if StoreModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error occured inserting the store"}, 500 # Internal server error

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        # alternate way 'items': [item.json() for item in self.items]
        stores = {'stores':list(map(lambda x: x.json(), StoreModel.query.all()))}
        return stores
