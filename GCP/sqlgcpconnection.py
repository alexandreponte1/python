from google.cloud.sql.connector import Connector
import sqlalchemy
project_id = "demo-project"
region = "us-central1"
instance_name = "demo-instance"
INSTANCE_CONNECTION_NAME = f"{project_id}:{region}:{instance_name}" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "root"
DB_PASS = "password"
# DB_NAME = "information_schema"


connector = Connector()
# function to return the database connection object
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
     results = db_conn.execute("SET PASSWORD FOR logan = 'alexandre'")
     print (results)
    #  for row in results:
    #     print(row)
connector.close()




