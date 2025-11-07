python -m venv .venv
source .venv/bin/activate


docker build -t flask-app .

docker run -d -p 5000:5000 flask-app


curl http://127.0.0.1:5000/store | jq