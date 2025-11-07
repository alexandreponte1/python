from flask import Flask, request


app = Flask(__name__)

@app.get("/") #http://127.0.0.1:5000/store
def index():
    return "GOKU, VEGETA KURIRIN"

if __name__ == "__main__":
    app.run(host="0.0.0.0.", port=5000, debug=True)