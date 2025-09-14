from db import get_cursor
from auth import new_teacher_register,teacher_login
connection,cur=get_cursor()

def add_class(standard,division,total_strength,class_teacher):
 
    try:

        connection.start_transaction()
        cur.execute('insert into classes(standard,division,total_strength,class_teacher) values(%s,%s,%s,%s)',(standard,division,total_strength,class_teacher))
        connection.commit()
        return True,'class created successfully'

    except Exception as e:
        connection.rollback()
        raise
    finally:
        cur.close()
        connection.close()


def remove_class(standard,division):

    try:
        connection.start_transaction()
        cur.execute('delete from classes where standard=%s and division = %s',(standard,division))
        connection.commit()
        return True,'class deleted successfully'
    
    except Exception as e:
        connection.rollback()
        raise

    finally:
        cur.close()
        connection.close()

        