def create_course(cursor,name):
    try:
        cursor.execute(f"insert into courses (name) values ({name})")
        return True
    except Exception as e:
        print(e)
        return False


def get_course_by_id(cursor, id):
    cursor.execute(f'select * from courses where id = {id}')
    return cursor.fetchone()


def get_last_course(cursor):
    cursor.execute(f"select * from courses order by id desc limit 1")
    return cursor.fetchone()
