from requests import get
from os import getenv
import base64
import json
import re
# export BEARER=$(gcloud auth print-access-token)
PROJECT = "active-chimera-359118"
BEARER = getenv("BEARER")
URL_SECRET = 'https://secretmanager.googleapis.com'
HEADERS = {'Authorization': 'Bearer {}'.format(BEARER)}

def get_secret_list():
    r = get(
        f'{URL_SECRET}/v1/projects/{PROJECT}/secrets', headers=HEADERS)
    return r.json().get('secrets')
    return []

secrets = get_secret_list()

for secret in secrets:
    name = secret.get("name").split("/")[3]
    print(name)




# curl "https://secretmanager.googleapis.com/v1/projects/projectID/secrets/test123?updateMask=labels" \
#     --request "PATCH" \
#     --header "authorization: Bearer $(gcloud auth print-access-token)" \
#     --header "content-type: application/json" \
#     --data "{'labels': {'goku': 'dragonball', 'gohan': 'dragonball' }}"






# curl -X GET -H "Authorization: Bearer "$(gcloud auth print-access-token) "https://secretmanager.googleapis.com/v1/projects/projectID/secrets"
# {
#   "secrets": [
#     {
#       "name": "projects/716970710829/secrets/kubernetesSecret123",
#       "replication": {
#         "automatic": {}
#       },
#       "createTime": "2022-09-01T17:52:30.906742Z",
#       "etag": "\"15e7a147066976\""
#     }
#   ],
#   "totalSize": 1
# }






# printf "senha bonita" | gcloud secrets create novosdsd112143 --data-file=- \
#   --replication-policy "user-managed" \
#   --locations "us-central1" \
#   --next-rotation-time="2022-12-12T09:00:00Z" \
#   --rotation-period="7776000s" \
#   --topics=projects/projectID/topics/secretTopicAlexandre \
#   --labels senha=banco,dominio=eu_com_br \
#   --project "projectID"




# ❯ python secretlist.py
# [{'name': 'projects/716970710829/secrets/segredoComLabel', 'replication': {'userManaged': {'replicas': [{'location': 'us-central1'}]}}, 'createTime': '2022-11-01T15:49:45.264206Z', 'labels': {'dominio': 'eu_com_br', 'senha': 'banco'}, 'topics': [{'name': 'projects/projectID/topics/secretTopicAlexandre'}], 'etag': '"15ec6aac51804e"', 'rotation': {'nextRotationTime': '2022-12-12T09:00:00Z', 'rotationPeriod': '7776000s'}}, {'name': 'projects/716970710829/secrets/test123', 'replication': {'userManaged': {'replicas': [{'location': 'us-central1'}]}}, 'createTime': '2022-10-27T17:39:34.328610Z', 'etag': '"15ec079fd9c522"'}]