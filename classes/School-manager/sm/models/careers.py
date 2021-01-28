def create_career(cursor,name):
    try:
        cursor.execute(f"insert into careers (name) values ({name})")
        return True
    except Exception as e:
        print(e)
        return False



def get_career_by_id(cursor, career_id):
    cursor.execute(f'select * from careers where id = {career_id}')
    return cursor.fetchone


def get_last_careers(cursor):
    cursor.execute(f"select * from careers order by id desc limit 1")
    return cursor.fetchone()


def get_career(cursor):
    cursor.execute('select * from careers')
    return cursor.fetchall()


def get_career_by_school(cursor, school_id):
    cursor.execute(f"""select c.id, c.name from careers c
    join schools_careers sc on sc.career_id = c.id
    join schools s on s.id  = sc.school_id 
    where s.id = {school_id}
    """)
    return cursor.fetchall()