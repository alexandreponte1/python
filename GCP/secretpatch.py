from email import header
from unittest.mock import patch
from requests import get
from requests import patch
from os import getenv
import base64
import json
import re
# export BEARER=$(gcloud auth print-access-token)
PROJECT = "projectID"
BEARER = getenv("BEARER")
URL_SECRET = 'https://secretmanager.googleapis.com'
HEADERS = {'Authorization': 'Bearer {}'.format(BEARER)}

def get_secret_list():
    r = get(
        f'{URL_SECRET}/v1/projects/{PROJECT}/secrets', headers=HEADERS)
    return r.json().get('secrets')
    return []

secrets = get_secret_list()

#add label
for secret in secrets:
    name = secret.get("name").split("/")[3]
    r = patch(
        f'{URL_SECRET}/v1/projects/{PROJECT}/secrets/{name}?updateMask=labels', headers=HEADERS, data="{'labels': {'agent': 'producao', 'stage': 'producao'}}")
    print(r)


#add topic
for secret in secrets:
    name = secret.get("name").split("/")[3]
    r = patch(
        f'{URL_SECRET}/v1/projects/{PROJECT}/secrets/{name}?updateMask=topics', headers=HEADERS, data="{'topics': {'name': 'projects/projectID/topics/secretTopicAlexandre'}}")
    print(r)




#add Rotation
for secret in secrets:
    name = secret.get("name").split("/")[3]
    r = patch(
        f'{URL_SECRET}/v1/projects/{PROJECT}/secrets/{name}?updateMask=rotation', headers=HEADERS, data="{'rotation': {'nextRotationTime': '2022-12-12T09:00:00Z', 'rotationPeriod': '7776000s'}}")
    print(r)


secrets = get_secret_list()

print(secrets)





#  curl "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID:addVersion" \
#     --request "POST" \
#     --header "authorization: Bearer $(gcloud auth print-access-token)" \
#     --header "content-type: application/json" \
#     --header "x-goog-user-project: project-id" \
#     --data "{\"payload\": {\"data\": \"${SECRET_DATA}\"}}"





# data="{'labels': {'goku': 'dragonball', 'gohan': 'dragonball'}}"


      # "topics": [{"name": "projects/projectID/topics/secretTopicAlexandre"}]
      # "{'topics': {'name': 'projects/projectID/topics/secretTopicAlexandre'}}"

#       'rotation': {'nextRotationTime': '2022-12-12T09:00:00Z', 'rotationPeriod': '7776000s'}

# curl "https://secretmanager.googleapis.com/v1/projects/projectID/secrets/test123?updateMask=topics" \
#     --request "PATCH" \
#     --header "authorization: Bearer $(gcloud auth print-access-token)" \
#     --header "content-type: application/json" \
#     --data "{'topics': {'name': 'projects/projectID/topics/secretTopicAlexandre'}}"








# # curl "https://secretmanager.googleapis.com/v1/projects/projectID/secrets/test123?updateMask=labels" \
# #     --request "PATCH" \
# #     --header "authorization: Bearer $(gcloud auth print-access-token)" \
# #     --header "content-type: application/json" \
# #     --data "{'labels': {'goku': 'dragonball', 'gohan': 'dragonball' }}"



# # curl -X GET -H "Authorization: Bearer "$(gcloud auth print-access-token) "https://secretmanager.googleapis.com/v1/projects/projectID/secrets"


# # import requests
 
# # # Making a PATCH request
# # r = requests.patch('https://httpbin.org / patch', data ={'key':'value'})
 
# # # check status code for response received
# # # success code - 200
# # print(r)
 
# # # print content of request
# # print(r.content)


# header="content-type: application/json"