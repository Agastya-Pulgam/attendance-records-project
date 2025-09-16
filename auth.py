from db import get_connection
from datetime import datetime
import bcrypt

def new_teacher_register(email,passwd,username):

   

    try:
        connection=get_connection()
        cur=connection.cursor(buffered=True)
        
        connection.start_transaction()
        cur.execute('select user_id from teacher_login where full_name = %s or email = %s', (username, email))

        if cur.fetchone():
            connection.rollback()
            return False,'user exists, try another name or email ID'
        
            
        pw_hash=bcrypt.hashpw(str(passwd).encode(),bcrypt.gensalt()).decode()

        cur.execute('insert into teacher_login(login_password,email,role,full_name) values(%s,%s,%s,%s)',(pw_hash,email,0,username))

        connection.commit()
        return True,'account created successfully'
    
    except Exception as e:
        connection.rollback()
        raise

    finally:
        cur.close()
        connection.close()


def teacher_login(username,email,password):
    
    try:
        connection=get_connection()
        cur=connection.cursor(buffered=True)

        connection.start_transaction()
        result=cur.execute('select login_password from teacher_login where email=%s and full_name=%s',(email,username))

        if result:
            stored_pw=result[0]
            if bcrypt.checkpw(str(password).encode(),stored_pw.encode()):
                return True,'login successful'
            else:
                return 'invalid credentials'
        else:
            return 'invalid credentials'
        
    except Exception as e:
        connection.rollback()
        raise
    finally:
        cur.close()
        connection.close()
