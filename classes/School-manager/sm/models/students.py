def create_student(cursor, person_id, career_id):
    try:
        query = "insert into students (person_id, career_id)"
        query += f"values ({person_id},{career_id})"
        cursor.execute(query)
        return True
    except Exception :
        return False


def get_students(cursor):
    cursor.execute("""
    select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
    join persons p on p.id = s.student_id
    join careers c on c.id = s.career_id;
    """)
    return cursor.fetchall()


def get_students_by_school(cursor, school_id):
    cursor.execute(f"""
        select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
        join persons p on p.id = s.student_id
        join careers c on c.id = s.career_id 
        join school_students ss on s.id = ss.student_id
        where s.id = {school_id};
        """)
    return cursor.fetchall()


def update_student(cursor, student_id, new_data):
    request = "update students set "
    items_length = len(new_data.values())
    item_count = 0
    for k, v in new_data.items():
        if item_count < items_length - 1:
            request += f" {k} = {v}, "
        else:
            request += f" {k} = {v} "
        item_count += 1
    try:
        request += f" where student_id = {student_id};"
        cursor.execute(request)
        return True
    except Exception:
        return False


def get_student_by_id(cursor, student_id):
    cursor.execute(f"""
    select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
    join persons p on p.id = s.student_id
    join careers c on c.id = s.career_id where student_id = {student_id};
    """)
    return cursor.fetchone()


def get_student_by_school_by_attendence_period(cursor, school_id, start_date, end_date):
    cursor.execute(f"""
        select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
        join persons p on p.id = s.student_id
        join careers c on c.id = s.career_id 
        join school_students ss on s.id = ss.student_id
        where registration_date between {start_date} and {end_date}
        and school_id = {school_id};
        """)
    return cursor.fetchall()


def get_graduated_student_by_promotion(cursor, school_id, graduation_date):
    cursor.execute(f"""
        select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
        join persons p on p.id = s.student_id
        join careers c on c.id = s.career_id 
        join school_students ss on s.id = ss.student_id
        where year(graduation_date) = {graduation_date}
        and school_id = {school_id};
        """)
    return cursor.fetchall()


def get_number_of_graduated_students_by_year_by_school(cursor):
    cursor.execute("""
        select sc.name, year(ss.graduation_date) as graduation_year, count(s.id) as number from schools_students ss
        join students s on s.id = ss.student_id
        join schools sc on ss.school_id = sc.id
        group by ss.school_id, graduation_year, sc.name;
        """)
    return cursor.fetchall()


def get_max_graduated_student_school(cursor):
    cursor.execute("""" 
        select school_name, max(total_graduated ) from
        (select name school_name, sum(number) as total_graduated from
        (select sc.name name, year(ss.graduation_date) as graduation_year, count(s.id) as number 
        from schools_students ss
        join students s on s.id = ss.student_id 
        join schools sc on sc.id = ss.school_id 
        group by ss.school_id,graduation_year,sc.name
        having graduation_year is not null
        order by ss.graduation_date));
        """)
    return cursor.fetchall()

def get_last_created_student(cursor):
    cursor.execute(f"""select * from students order by id
    desc limit 1""")
    return cursor.fetchone()