import os
import dotenv
import mysql.connector as msc

load_dotenv()

db_user=os.getenv("DB_USER")
db_pass=os.getenv("DB_PASS")
db_name=os.getenv("DB_NAME")
def get_cursor():

    mydb=msc.connect(
        host='localhost',
        user=db_user,
        passwd=db_pass,
        db=db_name
    )
    mycursor=mydb.cursor(buffered=True)
    
    print('connection successful' if mydb.is_connected() else 'failed to connect')

    return mydb,mycursor

