def get_student(cursor) :
    cursor.execute("""" 
    select s.id, p.firstname, p.lastname, p.age from student s
    join person p
    on s.id = p.student_id 
    join careers c
    on c.id = s.carer_id """)
    return cursor.fetchall()


def get_student_by_school(cursor, id) :
    cursor.execute("""" 
     select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
    join persons p
    on p.id = s.person_id 
    join careers c
    on c.id = s.career_id 
    join school_students ss
    on s.id = ss.student_id
    where ss.school_id = {};
    """.format(id))
    return cursor.fetchall()


def update_student(cursor, student, new_data) :
    request = "update students set"
    items_length = len(new_data.values())
    item_count = 0
    for k, v in new_data.items() :
        if item_count < items_length :
            request += f"{k} = {v},"
        else :
            request += f"{k} = {v},"
        item_count += 1
    try :
        request += f" where id = {student.id};"
        cursor.execute(request)
        return True
    except Exception :
        return False


def retreive_student(cursor, student_id) :
    cursor.execute(f"""select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
    join persons p on p.id = s.student_id
    join careers c on c.id = s.career_id where student_id = {student_id};""")
    return cursor.fetchall()


def get_student_history(cursor, school_id, date1, date2) :
    cursor.execute("""" 
     select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
    join persons p
    on p.id = s.person_id 
    join careers c
    on c.id = s.career_id 
    join school_students ss
    on s.id = ss.student_id
    where ss.school_id = {}
    and ss.registration_date between {} and {};
    """.format(school_id, date1, date2))
    return cursor.fetchall()


def get_student_graduated(cursor, school_id, date1) :
    cursor.execute("""" 

     select s.id, p.first_name, p.last_name, p.birthday, c.name from students s
    join persons p
    on p.id = s.person_id 
    join careers c
    on c.id = s.career_id 
    join school_students ss
    on s.id = ss.student_id
    where ss.school_id = {}
    and year(ss.graduation_date) = {};
    """.format(school_id, date1))
    return cursor.fetchall()


def get_student_number(cursor) :
    cursor.execute("""" 

    select sc.name, year(ss.graduation_date) as graduation_year, count(s.id) as number from schools_students ss
    join students s
    on s.id = ss.student_id 
    join school sc
    on sc.id = ss.school_id 
    group by ss.school_id,graduation_year,sc.name
    order by ss.graduation_date
    ;
    """)
    return cursor.fetchall()


def get_max_graduated_student(cursor) :
    cursor.execute("""" 
    select school_name, max(total_graduated ) from
    (select name school_name, sum(number) as total_graduated from
    (select sc.name name, year(ss.graduation_date) as graduation_year, count(s.id) as number 
    from schools_students ss
    join students s
    on s.id = ss.student_id 
    join school sc
    on sc.id = ss.school_id 
    group by ss.school_id,graduation_year,sc.name
    having graduation_year is not null
    order by ss.graduation_date))
    ;
    """)
    return cursor.fetchall()