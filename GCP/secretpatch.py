from email import header
from unittest.mock import patch
from requests import get
from requests import patch
from os import getenv
import base64
import json
import re
# export BEARER=$(gcloud auth print-access-token)
PROJECTID = "active-chimera-359118"
BEARER = getenv("BEARER")
URL_SECRET = 'https://secretmanager.googleapis.com'
HEADERS = {'Authorization': 'Bearer {}'.format(BEARER)}
# SECRET_DATA = getenv("SECRET_DATA")

def get_secret_list():
    r = get(
        f'{URL_SECRET}/v1/projects/{PROJECTID}/secrets', headers=HEADERS)
    return r.json().get('secrets')
    return []

secrets = get_secret_list()
print(secrets)

#add label
for secret in secrets:
    name = secret.get("name").split("/")[3]
    r = patch(
        f'{URL_SECRET}/v1/projects/{PROJECTID}/secrets/{name}?updateMask=labels', headers=HEADERS, data="{'labels': {'banco': 'sql', 'stage': 'dev'}}")
    print(r)


#add topic
for secret in secrets:
    name = secret.get("name").split("/")[3]
    r = patch(
        f'{URL_SECRET}/v1/projects/{PROJECTID}/secrets/{name}?updateMask=topics', headers=HEADERS, data="{'topics': {'name': 'projects/{active-chimera-359118}/topics/secretTopicAlexandre'}}")
    print(r)




#add Rotation
for secret in secrets:
    name = secret.get("name").split("/")[3]
    r = patch(
        f'{URL_SECRET}/v1/projects/{PROJECTID}/secrets/{name}?updateMask=rotation', headers=HEADERS, data="{'rotation': {'nextRotationTime': '2022-12-12T09:00:00Z', 'rotationPeriod': '7776000s'}}")
    print(r)


# #add new version
# for secret in secrets:
#     name = secret.get("name").split("/")[3]
#     r = patch(
#         f'{URL_SECRET}/v1/projects/{PROJECTID}/secrets/{name}:addVersion', headers=HEADERS, data="{'payload': {'data': '{SECRET_DATA}'}}")
#     print(r)



# No caso de adcionar uma nova versão do secret que seria basicamente a rotação, podemos fazer o seguinte:

# Configurar os secrets com rotação e pub/sub
# configurar uma cloudfunction para ser triggada peo pub/sub

# parsear os dados do pub/sub e pegar nome do secret e projeto.

# gerar uma senha aleatória.


# com essa senha aleatória salva em uma variavel, utilizar exemplo abaixo para adicionar uma nova versão com uma nova senha.




# SECRET_DATA=$(echo "carambacaracarao" | base64)


# curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets/criadoviaapi:addVersion" \
#     --request "POST" \
#     --header "authorization: Bearer $(gcloud auth print-access-token)" \
#     --header "content-type: application/json" \
#     --data "{\"payload\": {\"data\": \"${SECRET_DATA}\"}}"
### este

# data="{'payload': {'data': '${SECRET_DATA}'}}")

# data="{'labels': {'goku': 'lllllll', 'gohan': 'dragonball'}}")


# secrets = get_secret_list()

# print(secrets)








# # data="{'labels': {'goku': 'dragonball', 'gohan': 'dragonball'}}"


#       # "topics": [{"name": "projects/active-chimera-359118/topics/secretTopicAlexandre"}]
#       # "{'topics': {'name': 'projects/active-chimera-359118/topics/secretTopicAlexandre'}}"

# #       'rotation': {'nextRotationTime': '2022-12-12T09:00:00Z', 'rotationPeriod': '7776000s'}

# # curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets/test123?updateMask=topics" \
# #     --request "PATCH" \
# #     --header "authorization: Bearer $(gcloud auth print-access-token)" \
# #     --header "content-type: application/json" \
# #     --data "{'topics': {'name': 'projects/active-chimera-359118/topics/secretTopicAlexandre'}}"








# # # curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets/test123?updateMask=labels" \
# # #     --request "PATCH" \
# # #     --header "authorization: Bearer $(gcloud auth print-access-token)" \
# # #     --header "content-type: application/json" \
# # #     --data "{'labels': {'goku': 'dragonball', 'gohan': 'dragonball' }}"



# # # curl -X GET -H "Authorization: Bearer "$(gcloud auth print-access-token) "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets"


# # # import requests
 
# # # # Making a PATCH request
# # # r = requests.patch('https://httpbin.org / patch', data ={'key':'value'})
 
# # # # check status code for response received
# # # # success code - 200
# # # print(r)
 
# # # # print content of request
# # # print(r.content)


# # header="content-type: application/json"


# listar os secrets 

# curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets" \
#     --request "GET" \
#     --header "authorization: Bearer $(gcloud auth print-access-token)" \
#     --header "content-type: application/json"



# curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets/test123" \
#     --request "GET" \
#     --header "authorization: Bearer $(gcloud auth print-access-token)" \
#     --header "content-type: application/json"
