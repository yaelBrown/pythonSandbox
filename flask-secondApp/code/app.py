from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
  def get(self, name):
    return [i for i in items if i["name"] == name]

  def post(self, name):
    # gives error message if there is already a item with that name in list[]
    if next(filter(lambda x: x["name"] == name, items), None):
      return {"message": "An item with name '{}' already exists.".format(name)}, 400
    data = request.get_json(force=True) #force=true or silent=true
    item = {"name": name, "price": data["price"]}
    items.append(item)
    return item, 201

class ItemList(Resource):
  def get(self):
    return {"items": items}

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, '/items')

app.run(debug=True, port=5000)