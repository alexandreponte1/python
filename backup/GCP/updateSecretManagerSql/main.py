import base64
import json
import re
from sre_parse import ESCAPES
from google.cloud import secretmanager
from random import choice
import string
from google.cloud.sql.connector import Connector
import sqlalchemy


PROJECT_ID = "project_id"
SECRET_ID = "secret_id"


###Atualização secret

tamanho_da_senha = 10
caracteres = string.ascii_letters + string.digits
SENHA_SEGURA = ''
for i in range(tamanho_da_senha):
 SENHA_SEGURA += choice(caracteres)
payload = SENHA_SEGURA
print(SECRET_ID,PROJECT_ID)
client = secretmanager.SecretManagerServiceClient()
parent = f"projects/{PROJECT_ID}/secrets/{SECRET_ID}"
payload = payload.encode('UTF-8')

response = client.add_secret_version(
    request={
    "parent": parent,
    "payload": {"data": payload,}
    }
  )

print(f'Added secret version: {response.name}')
print(SECRET_ID, PROJECT_ID)
print("SEGREDO ATUALIZADO!!!")



###### Atualização senha do banco mysql


DB_USER = "root"
DB_PASS = "senha"
REGION = "us-central1"
instance_name = "bancodedados"
INSTANCE_CONNECTION_NAME = f"{PROJECT_ID}:{REGION}:{instance_name}" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")



response=client.access_secret_version(
    name=f'projects/{PROJECT_ID}/secrets/{SECRET_ID}/versions/latest'
)
SENHA = response.payload.data.decode("UTF-8")


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
# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
# connect to connection pool
with pool.connect() as db_conn:
     results = db_conn.execute(f"SET PASSWORD FOR logan = '{SENHA}'") # atualiza a senha do usuario logan
     print (results)
connector.close()