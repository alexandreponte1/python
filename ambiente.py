# from email import header
# from unittest.mock import patch
# from requests import get
# from requests import patch
from os import getenv
import os
# import base64
# import json
# import re
# # export BEARER=$(gcloud auth print-access-token)
# PROJECT = "projectID"
# BEARER = getenv("BEARER")
# URL_SECRET = 'https://secretmanager.googleapis.com'
# HEADERS = {'Authorization': 'Bearer {}'.format(BEARER)}


# export BEARER=$(gcloud auth print-access-token)
# export SECRET_DATA=$(echo "seCr3t" | base64)


# secrettest = os.system("export BEARER=$(gcloud auth print-access-token)")

# print(secrettest)
# os.environ["SECRET_DATA"] = str(secrettest)
# myenv = os.environ.get("SECRET_DATA")

# print(myenv)



import subprocess as sp
output = sp.getoutput('gcloud auth print-access-token')
# print (output)


os.environ["SECRET_DATA"] = str(output)
myenv = os.environ.get("SECRET_DATA")
print(myenv)



https://us-central1-active-chimera-359118.cloudfunctions.net/goku123