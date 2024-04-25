# from os import getenv
from requests import get
import base64
import json
import re
from google.cloud.sql.connector import Connector
import sqlalchemy
from google.cloud import secretmanager
from random import choice
import string
from os import getenv


###Filtrar os dados:
#PROJECT_ID = getenv("PROJECT_ID")

TOKEN = getenv("TOKEN")
ENVIROMENT = getenv("ENVIROMENT")
PRODUCT = getenv("PRODUCT")
URL_API = getenv("URL_API")
HEADERS = {'Authorization': (TOKEN)}

def get_secret_list():
    r = get(
        f'{URL_API}/{PRODUCT}/{ENVIROMENT}/?refresh=1', headers=HEADERS)
    return r.json()


apireturn =  get_secret_list()

get_secret_list()

print(apireturn)

###Para pegar o secret:
###Projeto
PROJECTID =apireturn["project_id"]
###Labels (project_id and namespace )
APPLABEL = apireturn["namespace"]

filter_str = f"labels.app:{APPLABEL} AND labels.project:{PROJECTID}"

###exemplo de como usar as labels para pegar a lista dos secrets:
print(f"gcloud --quiet secrets list '--filter=labels.app:{APPLABEL} AND labels.project:{PROJECTID}' --uri --project={PROJECTID}")

### listar os secrets Nesse caso preciso de mais informações para poder filtrar melhor os secrets
### os secrets de banco tem o nome com o mesmo final ex:  , isso pode facilitar o filtro
secretmanager_client = secretmanager.SecretManagerServiceClient()
parent = f"projects/{PROJECTID}"
for secret in secretmanager_client.list_secrets(request={"parent": parent, "filter": filter_str}):
    SECRET_ID = ((secret.name.split("/")[3]))
print(SECRET_ID)

### Pegar a senha dentro do secret e salvar em uma variavel:
response=secretmanager_client.access_secret_version(
    name=f'projects/{PROJECTID}/secrets/{SECRET_ID}/versions/latest'
)
OLDPASSWD = response.payload.data.decode("UTF-8")


###criar nova senha aleatoria e salvar em uma variavel
tamanho_da_senha = 10
caracteres = string.ascii_letters + string.digits
SENHA_SEGURA = ''
for i in range(tamanho_da_senha):
 SENHA_SEGURA += choice(caracteres)
NOVA_SENHA = SENHA_SEGURA


### alterar o secret no secret manager incluindo uma nova versão


parent = f"projects/{PROJECTID}/secrets/{SECRET_ID}"
payload = NOVA_SENHA.encode('UTF-8')

response = secretmanager_client.add_secret_version(
    request={
    "parent": parent,
    "payload": {"data": payload,}
    }
  )



### Atualização senha do banco mysql

DB_USER = apireturn["cloudsql_username"]
DB_PASS = OLDPASSWD
DB_PASS_NEW = payload
INSTANCE_CONNECTION_NAME = apireturn["cloudsql_connection"] ### demo-project:us-central1:demo-instance


connector = Connector()

def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db="",
    )
    return conn
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
with pool.connect() as db_conn:
     results = db_conn.execute(f"SET PASSWORD FOR {DB_USER} = '{DB_PASS_NEW}'")
     print (results)
connector.close()




