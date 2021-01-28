def create_teacher(cursor, person_id, career_id):
    try:
        query = "insert into teachers (person_id, career_id)"
        query += f"values ({person_id},{career_id})"
        cursor.execute(query)
        return True
    except Exception :
        return False


def get_teachers(cursor):
    cursor.execute("""
    select t.id, p.first_name, p.last_name, p.birthday, c.name from teachers t
    join persons p on p.id = t.person_id
    join careers c on c.id = t.career_id;
    """)
    return cursor.fetchall()


def get_teacher_by_school(cursor, school_id):
    cursor.execute(f"""
        select t.id, p.first_name, p.last_name, p.birthday, c.name from teachers t
        join persons p on p.id = t.person_id
        join careers c on c.id = t.career_id
        join school_teachers st on t.id = st.teacher_id
        where school_id = {school_id};
        """)
    return cursor.fetchall()


def update_teacher(cursor, teacher_id, new_data):
    request = "update teachers set "
    items_length = len(new_data.values())
    item_count = 0
    for k, v in new_data.items():
        if item_count < items_length - 1:
            request += f" {k} = {v}, "
        else:
            request += f" {k} = {v} "
        item_count += 1
    try:
        request += f" where teacher_id = {teacher_id};"
        cursor.execute(request)
        return True
    except Exception:
        return False


def get_teacher_by_id(cursor, teacher_id):
    cursor.execute(f"""
    select t.id, p.first_name, p.last_name, p.birthday, c.name from teachers t
    join persons p on p.id = t.person_id
    join careers c on c.id = t.career_id where t.id = {teacher_id};
    """)
    return cursor.fetchall()


def get_teachers_by_school_by_career(cursor, career_id, school_id):
    cursor.execute(f"""
    select t.id, p.first_name, p.last_name, p.birthday from teachers t
    join persons p on p.id = t.person_id
    join careers c on c.id = t.career_id 
    join schools_teachers st on st.teacher_id = t.id 
    where c.id = {career_id} and st.school_id = {school_id}
    """)
    return cursor.fetchall()

def get_last_created_teacher(cursor):
    cursor.execute(f"""select * from teachers order by id
    desc limit 1""")
    return cursor.fetchone()
