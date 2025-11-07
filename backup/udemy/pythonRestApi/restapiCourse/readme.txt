python -m venv .venv
source .venv/bin/activate

flask run


curl http://127.0.0.1:5000/store | jq
