from flask import request, jsonify
from flask_restful import Resource, Api, reqparse, abort

from app.models.shopping_list_models import ShoppingListModel
# from app.models.shopping_item_models import ShoppingItemModel

# todo: move to sqlalchemy 
shoppings = {'shopping1': {'item': 'shopping 1'}}


def abort_if_shopping_doesnt_exist(shopping_id):
    if shopping_id not in shoppings:
        abort(404, message="Shopping List {} doesn't exist".format(shopping_id))

parser = reqparse.RequestParser()
parser.add_argument('item')

class ShoppingApi(Resource):
    def get(self, shopping_id):
        abort_if_shopping_doesnt_exist(shopping_id)
        return shoppings[shopping_id]
    
    def delete(self, shopping_id):
        abort_if_shopping_doesnt_exist(shopping_id)
        del shoppings[shopping_id]
        return '', 204

    def put(self, shopping_id):
        args = parser.parse_args()
        item = {'item': args['item']}
        shoppings[shopping_id] = item
        return item, 201


class ShoppingListApi(Resource):
    def get(self):
        # shoppingListData = ShoppingListModel.get_all()
        # results = []
        # for shoppingList in shoppingListData:
        #     obj = {
        #         'id': shoppingList.id,
        #         'store_name': shoppingList.store_name,
        #         'date_created': shoppingList.date_created,
        #         'date_modified': shoppingList.date_modified
        #     }
        #     results.append(obj)

        # response = jsonify(results)
        response.status_code = 200
        return response
    
    def post(self):
        args = parser.parse_args()
        # shopping_id = int(max(shopping.keys()).lstrip('shopping')) + 1
        # shopping_id = 'shopping%i' % shopping_id
        # shoppings[shopping_id] = {'item': args['item']}
        # return shoppings[shopping_id], 201
        store_name = str(request.data.get('store_name', ''))
        # if store_name:
        #     shoppingListData = ShoppingListModel(name=store_name)
        #     shoppingListData.save()
        #     response = jsonify({
        #         'id': shoppingListData.id,
        #         'store_name': shoppingListData.store_name,
        #         'date_created': shoppingListData.date_created,
        #         'date_modified': shoppingListData.date_modified
        #     })

        response.status_code = 201
        return response
