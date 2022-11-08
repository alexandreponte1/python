from email import header
from unittest.mock import patch
from requests import get
from requests import patch
from requests import post
from os import getenv
import base64
import json
import re

PROJECT = "active-chimera-359118"
BEARER = getenv("BEARER")
URL_SECRET = 'https://secretmanager.googleapis.com'
HEADERS = {'Authorization': 'Bearer {}'.format(BEARER)}
SECRET_DATA = "senha123"


# Listar os secrets
def get_secret_list():
    r = get(
        f'{URL_SECRET}/v1/projects/{PROJECT}/secrets', headers=HEADERS)
    return r.json().get('secrets')

secrets = get_secret_list()

print(secrets)

#add nova versão
for secret in secrets:
    name = secret.get("name").split("/")[3]
    r = post(
        f'{URL_SECRET}/v1/projects/{PROJECT}/secrets/{name}:addVersion', headers=HEADERS, data="{\"payload\": {\"data\": \"{SECRET_DATA}\"}}")
    print(r)







#  curl "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID:addVersion" \
#     --request "POST" \
#     --header "authorization: Bearer $(gcloud auth print-access-token)" \
#     --header "content-type: application/json" \
#     --header "x-goog-user-project: project-id" \
#     --data "{\"payload\": {\"data\": \"${SECRET_DATA}\"}}"


# # curl "https://secretmanager.googleapis.com/v1/projects/projectID/secrets/test123?updateMask=labels" \
# #     --request "PATCH" \
# #     --header "authorization: Bearer $(gcloud auth print-access-token)" \
# #     --header "content-type: application/json" \
# #     --data "{'labels': {'goku': 'dragonball', 'gohan': 'dragonball' }}"

