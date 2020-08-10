from flask import Flask, redirect, url_for, jsonify, request

app = Flask(__name__)

stores = [
  {
    'name': 'My first store',
    'items': [
      {
        'name': 'Hammer',
        'price': 15.99
      }
    ]
  },
  {
    'name': 'yael',
    'items': [
      {
        'name': 'Lemonade',
        'price': 27.00
      }
    ]
  }
]

@app.route("/")
def home():
  return "<h1>Hello from Flask!</h1>"

@app.route("/<name>")
def user(name):
  return f"Hello {name}"

@app.route("/api/admin")
def admin():
  return redirect(url_for(home))


# Example GET and POST from tutorial
@app.route("/api/store")
def get_store():
  return jsonify({'stores': stores})

@app.route("/api/store/<string:name>", methods=["POST"])
def create_store(name):
  request_data = request.get_json()
  print(request_data)
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)

@app.route("/api/store/<string:name>")
def getOne_store(name):
  reqStore = [s for s in stores if s["name"] == name]
  if reqStore[0] == False: return jsonify({"msg": "Store not found"})
  return jsonify({"store": reqStore})

@app.route("/api/store/<string:name>/items", methods=["POST"])
def create_item(name):
  pass

@app.route("/api/store/<string:name>/items")
def get_items(name):
  reqStore = [s["items"] for s in stores if s["name"] == name]
  if reqStore[0] == False: return jsonify({"msg": "Store not found"})
  return jsonify({"msg": reqStore})

if __name__ == "__main__":
  app.run(debug=True)