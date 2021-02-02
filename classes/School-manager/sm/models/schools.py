def create_school(cursor,name):
    try:
        query = f"insert into schools (name) values ('{name}')"
        print(query)
        cursor.execute(query)
        return True
    except Exception as e:
        print(e)
        return False



def get_school_by_id(cursor, school_id):
    cursor.execute(f'select * from schools where id = {school_id}')
    return cursor.fetchone()


def get_last_schools(cursor):
    cursor.execute(f"select * from schools order by id desc limit 1")
    return cursor.fetchone()


def get_schools(cursor):
    cursor.execute('select * from schools')
    return cursor.fetchall()