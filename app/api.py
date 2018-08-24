from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with

resource_fields = {
    'item':   fields.String,
    # 'uri':    fields.Url('shopping_ep')
}

class ShoppingDao(object):
    def __init__(self, shopping_id, item):
        self.shopping_id = shopping_id
        self.item = item

        self.status = 'active'


# todo: move to sqlalchemy 
shoppings = {'shopping1': {'item': 'shopping 1'}}


def abort_if_shopping_doesnt_exist(shopping_id):
    if shopping_id not in shoppings:
        abort(404, message="Shopping List {} doesn't exist".format(shopping_id))

parser = reqparse.RequestParser()
parser.add_argument('item')

class Shopping(Resource):
    @marshal_with(resource_fields)
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


class ShoppingList(Resource):
    def get(self):
        return shoppings
    
    def post(self):
        args = parser.parse_args()
        shopping_id = int(max(shopping.keys()).lstrip('shopping')) + 1
        shopping_id = 'shopping%i' % shopping_id
        shoppings[shopping_id] = {'item': args['item']}
        return shoppings[shopping_id], 201
