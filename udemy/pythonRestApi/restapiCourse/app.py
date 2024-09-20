import uuid
from flask import Flask, request, render_template
from db import items, stores

app = Flask(__name__)

# stores = [
#     {
#         "name": "My Store",
#         "items": [
#             {
#             "name":"chair",
#             "price": 15.99
#             }
#         ]
#     }
# ]



# stores = {}
# items = {
#     1: {
#         "name": "Chair",
#         "price": 17.99
#     },
#     2: {
#         "name": "Table",
#         "price": 180.50
#     }
# }


goku = "Oi eu sou o Goku!!!!"

@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item, 201


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        # Here you might also want to add the items in this store
        # We'll do that later on in the course
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404




@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}





# @app.get("/") #http://127.0.0.1:5000/store
# def get_goku():
#     return goku


@app.get("/")
def get_index():
    return render_template("index.html")