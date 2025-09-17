from db import get_connection
from auth import new_teacher_register,teacher_login

def add_class(standard,division,total_strength,class_teacher):
 
    try:
        connection=get_connection()
        cur=connection.cursor(buffered=True)

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
        connection=get_connection()
        cur=connection.cursor(buffered=True)

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

# BELOW GIVEN FUNCTION IS USE TO EDIT CLASS DETAILS, SUCH AS CLASS TEACHER,TOTAL STRENGTH, STANDARD AND DIVISION AN 
# AN EXAMPLE CASE OF THIS IS WHEN A CLASS IS PROMOTED TO A HIGHER GRADE, INSTEAD OF CREATING A NEW CLASS FOR PRE-EXISTNG STUDENTS,
# THE TEACHER CAN JUST EDIT THE CLASS STANDARD, SAVING TIME FROM FILLING OUT THE DETAILS OF THE CLASS AGAIN


def modify_class(class_id, new_standard=None, new_division=None, new_strength=None):

    try:
        connection=get_connection()
        cur=connection.cursor(buffered=True)
        fields=[]
        values=[]
        connection.start_transaction()
        if new_standard:

            fields.append('standard=%s')
            values.append(new_standard)

        elif new_division:
            
            fields.append('division=%s')
            values.append(new_division)

        elif new_strength:

            fields.append('total_strength=%s')
            values.append(new_strength)

        if not fields:
            return {'status':'error','message':'no fields to update'}

        cur.execute(f'update classes set{', '.join(fields)} where class_id = %s',(values.append(class_id)))
        connection.commit()
        
        return {'status':'ok','updated':cur.rowcount}
    
    except Exception as e:
        connection.rollback()
        return {'status':'error','message':str(e)}
    
    finally:
        cur.close()
        connection.close()