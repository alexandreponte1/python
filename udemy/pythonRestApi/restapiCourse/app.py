from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
            "name":"chair",
            "price": 15.99
            }
        ]
    }
]


# stores = "Oi eu sou o Goku!!!!"

@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}



