import os
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()
secret_name = "my-secret"
project_id = "PROJECT_ID"
request = {"name": f"projects/{project_id}/secrets/{secret_name}/versions/latest"}
response = client.access_secret_version(request)
secret_string = response.payload.data.decode("UTF-8")


def secret_hello(request):
    return secret_string



# PROJECT_ID@appspot.gserviceaccount.com


# $ gcloud secrets add-iam-policy-binding my-secret \
#     --role roles/secretmanager.secretAccessor \
#     --member serviceAccount:PROJECT_ID@appspot.gserviceaccount.com