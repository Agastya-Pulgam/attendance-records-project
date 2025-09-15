import os
import dotenv
from mysql.connector import pooling


dotenv.load_dotenv()

db_user=os.getenv("DB_USER")
db_pass=os.getenv("DB_PASS")
db_name=os.getenv("DB_NAME")

pool=pooling.get_MySQLConnectionPool(
    
    poolname='mypool',
    pool_size=50,
    host='localhost',
    user=db_user,
    passwd=db_pass,
    db=db_name
)

def get_connection():

    return pool.get_connection()

try:
    connection=get_connection()
    if connection.is_connected():
        print('connection successful, ready to proceed')
    connection.close()
except Exception as e:
    print('connection failed: ',e)