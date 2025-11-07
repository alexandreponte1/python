from google.cloud import secretmanager
from random import choice
import string


def add_secret_version(secret_id, payload):
    # secret_id  = "my-secret"
    PROJECT_ID = "pruebasecret-360520"


    client = secretmanager.SecretManagerServiceClient()

    parent = f"projects/{PROJECT_ID}/secrets/{secret_id}"

    payload = payload.encode('UTF-8')

    response = client.add_secret_version(parent=parent, payload={'data': payload})

    print(f'Added secret version: {response.name}')
    return response



def senhasegura():
  tamanho_da_senha = 10
  caracteres = string.ascii_letters + string.digits
  # caracteres = string.ascii_letters + string.digits + string.punctuation
  senha_segura = ''
  for i in range(tamanho_da_senha):
    senha_segura += choice(caracteres)
  return senha_segura


pwdnow = senhasegura()


add_secret_version("ponte123", pwdnow)
