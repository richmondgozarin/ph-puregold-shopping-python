from flask import request, jsonify
from flask_restful import Resource, Api, reqparse, abort

from app.models.shopping_list import ShoppingList
from app.models.item import Item

parser = reqparse.RequestParser()

# ShoppingListApi
# shows a list of all shopping records, 
# and lets you POST to add new shopping list
class ShoppingListApi(Resource):
    def get(self, shopping_id=None):
        if shopping_id != None:
            shoppingListData = ShoppingList.get_all_by_id(shopping_id)
        else:
            shoppingListData = ShoppingList.get_all()

        results = []
        for shoppingList in shoppingListData:
            shopping_items = []
            for item in shoppingList.items:
                obj_item = {
                    'id': item.item_id,
                    'quantity': item.quantity,
                    'item_name': item.item_name,
                    'date_created': item.date_created,
                    'shopping_id': item.shopping_id
                }
                shopping_items.append(obj_item)

            obj = {
                'id': shoppingList.shopping_id,
                'store_name': shoppingList.store_name,
                'items': shopping_items,
                'date_created': shoppingList.date_created
            }
            results.append(obj)

        response = jsonify(results)
        response.status_code = 200
        return response
    
    def post(self):
        store_name = str(request.data.get('store_name', ''))
        
        if store_name:
            shoppingList = ShoppingList(name=store_name)
            shoppingList.save()
            response = jsonify({
                'id': shoppingList.shopping_id,
                'store_name': shoppingList.store_name,
                'items': shoppingList.items,
                'date_created': shoppingList.date_created
            })
            response.status_code = 200
            return response
        else:
            response = jsonify({
                "error_code": 302,
                "error_message": "No store name provided"
            })
            response.status_code = 302
            return response

    def put(self, shopping_id=None):
            
        store_name = str(request.data.get('store_name', ''))

        if shopping_id:
            shopping_items = []
            shoppingList = ShoppingList.get_by_id(shopping_id)
            shoppingList.update(store_name)

            for item in shoppingList.items:
                obj_item = {
                    'id': item.item_id,
                    'quantity': item.quantity,
                    'item_name': item.item_name,
                    'date_created': item.date_created,
                    'shopping_id': item.shopping_id
                }
                shopping_items.append(obj_item)
                
            response = jsonify({
                'id': shoppingList.shopping_id,
                'store_name': shoppingList.store_name,
                'items': shoppingList.items,
                'date_created': shoppingList.date_created
            })
            response.status_code = 200
            return response  
        else:
            response = jsonify({
                "error_code": 302,
                "error_message": "No store name provided"
            })
            response.status_code = 302
            return response
    
    def delete(self, shopping_id=None):
        shoppingList = ShoppingList.get_by_id(shopping_id)
        if shoppingList:
            shoppingList.delete()
            return "item deleted", 200
        else:
            response = jsonify({
                "error_code": 302,
                "error_message": "Shopping Id does not exist."
            })
            response.status_code = 302
            return response      


# ShoppingItemApi
# shows a list of all shopping item records, 
# and lets you POST to shopping item
class ShoppingItemApi(Resource):
    def get(self, item_id=None):
        if item_id != None:
            items = Item.get_all_by_id(item_id)
        else:
            items = Item.get_all()

        results = []
        for item in items:
            obj = {
                'id': item.item_id,
                'quantity': item.quantity,
                'item_name': item.item_name,
                'date_created': item.date_created
            }
            results.append(obj)

        response = jsonify(results)
        response.status_code = 200
        return response

    def post(self, shopping_id=None):
        quantity = int(request.data.get('quantity', 0))
        item_name = str(request.data.get('item_name', ''))

        if shopping_id != None and item_name != None and quantity != 0:
            item = Item(name=item_name)
            item.shopping_id = shopping_id
            item.quantity = quantity
            item.save()
            response = jsonify({
                'id': item.item_id,
                'quantity': item.quantity,
                'item_name': item.item_name,
                'date_created': item.date_created
            })
            response.status_code = 201
            return response
        else:
            response = jsonify({
                "error_code": 302,
                "error_message": "Missing parameters"
            })
            response.status_code = 302
            return response