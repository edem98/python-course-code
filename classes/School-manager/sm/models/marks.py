def insert_mark(cursor, mark, course_id, student_id):
    try:
        query = "insert into marks (mark, course_id, student_id)"
        query += f"values ({mark},{course_id},{student_id})"
        cursor.execute(query)
        return True
    except Exception :
        return False




def get_marks(cursor):
    cursor.execute("""
    select m.mark, co.name, p.first_name, p.last_name, c.name from marks m
    join students s on m.student_id = s.id
    join courses co on m.course_id = co.id 
    join persons p on p.id = s.person_id
    join careers c on c.id = s.career_id
    join school_students ss on s.id = ss.student_id
    group by c.name 
    order by co.name;
    """)
    return cursor.fetchall()


def get_marks_by_course_by_school(cursor, course_id, student_id, school_id):
    cursor.execute(f"""
    select m.mark, p.first_name, p.last_name from marks m
    join persons p on p.id = s.person_id
    join students s on m.student_id = s.id
    join courses co on m.course_id = co.id 
    join schools_students ss on ss.student_id = s.id 
    join school sc on sc.id = ss.school_id
    where co.id = {course_id} and s.id = {student_id} and ss.school_id = {school_id}
    """)
    return cursor.fetchall()