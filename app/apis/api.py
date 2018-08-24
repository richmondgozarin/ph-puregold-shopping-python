from flask import request, jsonify
from flask_restful import Resource, Api, reqparse, abort

from app.models.shopping_list import ShoppingList
from app.models.item import Item

parser = reqparse.RequestParser()

# ShoppingListApi
# shows a list of all shopping records, 
# and lets you POST to add new shopping list
class ShoppingListApi(Resource):
    def get(self, store_name=None):
        if store_name:
            shoppingListData = ShoppingList.get_by_store_name(store_name)
        else: 
            shoppingListData = ShoppingList.get_all()

        results = []
        if shoppingListData:
            for shoppingList in shoppingListData:
                obj = {
                    'id': shoppingList.id,
                    'store_name': shoppingList.store_name,
                    'items': shoppingList.items,
                    'date_created': shoppingList.date_created,
                    'date_modified': shoppingList.date_modified
                }
                results.append(obj)

        response = jsonify(results)
        response.status_code = 200
        return response
    
    def post(self):
        args = parser.parse_args()
        store_name = str(request.data.get('store_name', ''))
        if store_name:
            shoppingListData = ShoppingList(name=store_name)
            shoppingListData.save()
            response = jsonify({
                'id': shoppingListData.id,
                'store_name': shoppingListData.store_name,
                'items': shoppingListData.items,
                'date_created': shoppingListData.date_created,
                'date_modified': shoppingListData.date_modified
            })
            response.status_code = 200
        else:
            abort(204, message="No store name provided")
        return response

    def put(self):
        args = parser.parse_args()
        store_name = str(request.data.get('store_name', ''))
        if store_name:
            shoppingListData = ShoppingList(name=store_name)
            shoppingListData.update()
            response = jsonify({
                'id': shoppingListData.id,
                'store_name': shoppingListData.store_name,
                'items': shoppingListData.items,
                'date_created': shoppingListData.date_created,
                'date_modified': shoppingListData.date_modified
            })
            response.status_code = 200
        else:
            abort(204, message="No store name provided")
        return response  
    
    def delete(self, id=None):
        ShoppingList.delete(id)
        return '', 200


# ShoppingItemApi
# shows a list of all shopping item records, 
# and lets you POST to shopping item
class ShoppingItemApi(Resource):
    
    def post(self):
        args = parser.parse_args()
        quantity = int(request.data.get('quantity', 0))
        item_name = str(request.data.get('item_name', ''))

        if item_name:
            shoppingListData = ShoppingListModel(name=store_name)
            shoppingListData.save()
            response = jsonify({
                'id': data.id,
                'quantity': data.quantity,
                'item_name': data.item_name,
                'date_created': data.date_created,
                'date_modified': data.date_modified
            })
            response.status_code = 201
        else:
            abort(204, message="No item name provided")
        return response