import mysql.connector as msc

def get_cursor():

    mydb=msc.connect(
        host='localhost',
        user='root',
        passwd='pulgamagastya29@gmail.com',
        db='attendance_records'
    )
    mycursor=mydb.cursor(buffered=True)
    
    print('connection successful' if mydb.is_connected() else 'failed to connect')

    return mydb,mycursor

